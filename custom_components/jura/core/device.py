import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, TypedDict
from zipfile import ZipFile

import xmltodict
from bleak import AdvertisementData, BLEDevice

from .client import Client

_LOGGER = logging.getLogger(__name__)

COMMAND_TIME = 15
SELECTS = [
    "product",  # 1
    "grinder_ratio",  # 2
    "coffee_strength",  # 3
    "temperature",  # 7
]

NUMBERS = [
    "water_amount",  # 4
    "milk_amount",  # 5
    "milk_foam_amount",  # 6
    "bypass",  # 10
    "milk_break",  # 11
]


class Attribute(TypedDict, total=False):
    options: list[str]
    default: str

    min: int
    max: int
    step: int
    value: int

    is_on: bool
    extra: dict


class Device:
    def __init__(
        self,
        name: str,
        model: str,
        products: list,
        alerts: dict[int, str],
        key: int,
        device: BLEDevice,
    ):
        self.name = name
        self.model = model
        self.products = products
        self.alerts = alerts

        self.client = Client(device, self.set_connected, key)

        self.connected = False
        self.conn_info = {"mac": device.address}

        self.options = get_options(self.products)

        self.product = None
        self.values = None
        self.updates_connect: list = []
        self.updates_product: list = []
        self.updates_statistics = []
        self.updates_alerts = []
        self.statistics = {"total_products": None, "product_counts": {}}
        self.active_alerts = {}

    @property
    def mac(self) -> str:
        return self.client.device.address

    def register_update(self, attr: str, handler: Callable):
        if attr == "product":
            return
        elif attr == "connection":
            self.updates_connect.append(handler)
        else:
            self.updates_product.append(handler)

    def update_ble(self, advertisment: AdvertisementData):
        self.conn_info["last_seen"] = datetime.now(timezone.utc)
        self.conn_info["rssi"] = advertisment.rssi

        for handler in self.updates_connect:
            handler()

    def set_connected(self, connected: bool):
        self.connected = connected

        for handler in self.updates_connect:
            handler()

    def selects(self) -> list[str]:
        products = str(self.products).lower()
        return [k for k in SELECTS if k in products]

    def numbers(self) -> list[str]:
        products = str(self.products).lower()
        return [k for k in NUMBERS if k in products]

    def attribute(self, attr: str) -> Attribute:
        if attr == "connection":
            return Attribute(is_on=self.connected, extra=self.conn_info)

        if attr == "product":
            return Attribute(
                options=[
                    i["@Name"] for i in self.products if i.get("@Active") != "false"
                ],
                default=self.product["@Name"] if self.product else None,
            )

        attribute = self.product and self.product.get(attr.upper())
        if not attribute:
            return {"options": self.options[attr]} if attr in self.options else {}

        if "@Value" in attribute:
            return Attribute(
                min=int(attribute["@Min"]),
                max=int(attribute["@Max"]),
                step=int(attribute["@Step"]),
                value=int(attribute["@Value"]),
            )

        default = attribute["@Default"]
        return Attribute(
            options=[i["@Name"] for i in attribute["ITEM"]],
            default=next(
                i["@Name"] for i in attribute["ITEM"] if i["@Value"] == default
            ),
        )

    def select_option(self, attr: str, option: str):
        if attr == "product":
            self.select_product(option)
            return

        attribute = self.product and self.product.get(attr.upper())
        if not attribute:
            return None

        value = next(i["@Value"] for i in attribute["ITEM"] if i["@Name"] == option)
        self.set_value(attr, int(value, 16))

    def set_value(self, attr: str, value: int):
        self.client.ping()

        self.values[attr] = value

    def select_product(self, product: str):
        self.client.ping()

        self.product = next(i for i in self.products if i["@Name"] == product)
        self.values = {}

        # dispatch to all listeners
        for handler in self.updates_product:
            handler()

    def start_product(self):
        if self.product:
            self.client.send(self.command())

    def command(self) -> bytes:
        data = bytearray(18)

        # set product
        data[1] = int(self.product["@Code"], 16)

        for attr in SELECTS + NUMBERS:
            attribute = self.product and self.product.get(attr.upper())
            if not attribute:
                continue

            if attr in self.values:
                # set user's value
                value = self.values[attr]
            elif "@Value" in attribute:
                # set default int value
                value = int(attribute["@Value"])
            else:
                # set default list value
                value = int(attribute["@Default"], 16)

            if step := int(attribute.get("@Step", 0)):
                value = int(value / step)

            pos = int(attribute["@Argument"][1:])
            data[pos] = value

        # additional data (some unknown)
        # data[0] = self.client.key
        # data[9] = 1
        # data[16] = 6
        # need to be set or the machine will go into a half broken state
        data[17] = self.client.key

        return data

    # Add method to register statistics updates
    def register_statistics_update(self, handler: Callable):
        """Register a callback for statistics updates."""
        self.updates_statistics.append(handler)

    async def read_statistics(self, force_update: bool = False):
        """Read statistics from the machine."""

        _LOGGER.debug("Reading Jura statistics...")

        # Read statistics data from client
        decrypted_data = await self.client.read_statistics_data()
        if decrypted_data is None:
            _LOGGER.debug(
                "Failed to read statistics data, returning existing statistics"
            )
            return self.statistics

        # Convert all 3-byte chunks to integers
        product_counts_array = []
        for i in range(0, len(decrypted_data), 3):
            if i + 3 <= len(decrypted_data):
                # Convert 3 bytes to an integer
                count = int.from_bytes(decrypted_data[i : i + 3], "big")
                if count == 0xFFFF:  # means 0 it seems
                    count = 0
                product_counts_array.append(count)

        # get total_count from first 3 bytes if available
        total_count = (
            product_counts_array[0]
            if product_counts_array and product_counts_array[0] is not None
            else None
        )
        _LOGGER.info(
            f"Total coffee count from data: {total_count if total_count is not None else 'undefined'}"
        )

        # remove aberrant values if any
        if total_count == 0 or total_count > 1000000:
            _LOGGER.info(
                "total 0 or too high, something's wrong, returning existing statistics"
            )
            return self.statistics

        # get the names associated to the products counts
        product_counts = {}
        for i, count in enumerate(product_counts_array):
            if i == 0:  # Skip the total
                continue

            product = next((p for p in self.products if int(p["@Code"], 16) == i), None)
            if product:
                product_counts[product["@Name"]] = count
                _LOGGER.debug(
                    f"Stat entry: Position {i} = {count} -> {product['@Name']}"
                )
            else:
                _LOGGER.debug(f"No product found for code {i} with count {count}")

        # Log the final counts at info log level
        for product, count in product_counts.items():
            _LOGGER.info(f"Product: {product}, Count: {count}")

        # Save the statistics
        self.statistics = {
            "total_products": total_count,
            "product_counts": product_counts,
        }

        # Notify all statistics listeners
        _LOGGER.debug(f"Notifying {len(self.updates_statistics)} statistics listeners")
        for handler in self.updates_statistics:
            handler()

        return self.statistics

    def register_alert_update(self, handler: Callable):
        """Register a callback for alert updates."""
        self.updates_alerts.append(handler)
        # Trigger an immediate update for the new handler
        if self.active_alerts:
            handler()

    async def read_alerts(self) -> dict:
        """Read alerts from the machine."""

        # Read machine status data from client
        data = await self.client.read_machine_status()
        if data is None:
            _LOGGER.debug("Failed to read machine status data")
            return self.active_alerts

        # Process alert bits
        alerts = {}
        for i in range((len(data) - 1) * 8):
            offset_abs = (i >> 3) + 1
            offset_byte = 7 - (i & 0b111)
            if (data[offset_abs] >> offset_byte) & 0b1:
                alerts[i] = alert = self.alerts.get(i, f"unknown alert {i}")
                _LOGGER.debug(f"Alert active. Alert bit: {i} - {alert}")

        # Save the alerts
        self.active_alerts = alerts

        # Notify all alert listeners
        _LOGGER.debug(f"Notifying {len(self.updates_alerts)} alert listeners")
        for handler in self.updates_alerts:
            handler()

        return self.active_alerts


class EmptyModel(Exception):
    pass


class UnsupportedModel(Exception):
    pass


def get_machine(adv: bytes) -> dict | None:
    model_id = int.from_bytes(adv[4:6], "little")
    if model_id == 0:
        raise EmptyModel()

    path = Path(__file__).parent / "resources.zip"
    with ZipFile(path) as f:
        prefix = str(model_id).encode()
        with f.open("JOE_MACHINES.TXT") as txt:
            try:
                line = next(i for i in txt.readlines() if i.startswith(prefix))
            except StopIteration:
                raise UnsupportedModel(model_id)
            items = line.decode().split(";")

        dirname = f"documents/xml/{items[2].upper()}/"
        filename = next(
            i.filename
            for i in f.filelist
            if i.filename.startswith(dirname) and i.filename.endswith(".xml")
        )

        with f.open(filename) as xml:
            raw = xmltodict.parse(xml.read())
            products = raw["JOE"]["PRODUCTS"]["PRODUCT"]

            try:
                alerts = {
                    int(i["@Bit"]): i["@Name"] for i in raw["JOE"]["ALERTS"]["ALERT"]
                }
            except:
                alerts = {}

    # First byte is the encryption key
    return {"model": items[1], "products": products, "alerts": alerts, "key": adv[0]}


def get_options(products: list[dict]) -> dict[str, list]:
    return {
        attr: list(
            {
                option["@Name"]: None
                for product in products
                for option in product.get(attr.upper(), {}).get("ITEM", [])
            }.keys()  # unique keys with save order
        )
        for attr in SELECTS
    }
