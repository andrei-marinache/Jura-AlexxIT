import logging

from bleak import BLEDevice
from homeassistant.components import bluetooth
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback

from .core import DOMAIN
from .core.device import Device, EmptyModel, UnsupportedModel, get_machine

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["binary_sensor", "number", "select", "switch", "sensor", "text", "button"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    devices = hass.data.setdefault(DOMAIN, {})

    @callback
    def create_device(adv: bytes, ble_device: BLEDevice) -> Device | None:
        try:
            machine = get_machine(adv)
        except EmptyModel:
            return None
        except UnsupportedModel as e:
            _LOGGER.error("Unsupported model: %s", *e.args)
            return None

        devices[entry.entry_id] = device = Device(
            entry.title,
            machine["model"],
            machine["products"],
            machine["maintenance_counters"],
            machine["maintenance_percents"],
            machine["alerts"],
            machine["key"],
            ble_device,
        )
        hass.create_task(
            hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
        )
        return device

    @callback
    def update_ble(
        service_info: bluetooth.BluetoothServiceInfoBleak,
        change: bluetooth.BluetoothChange,
    ) -> None:
        _LOGGER.debug(f"{change} {service_info.advertisement}")

        if device := devices.get(entry.entry_id):
            # connect through the path the machine was last heard on
            device.client.device = service_info.device
            device.update_ble(service_info.advertisement)
            return

        adv = service_info.advertisement.manufacturer_data[171]
        if device := create_device(adv, service_info.device):
            device.update_ble(service_info.advertisement)
            hass.config_entries.async_update_entry(entry, data={**entry.data, "adv": adv.hex()})

    # The machine only advertises while it is switched on. Set up from the advertisement
    # saved last time, so the entities exist (with their restored states) while it is off.
    if adv := entry.data.get("adv"):
        mac = entry.data["mac"]
        ble_device = bluetooth.async_ble_device_from_address(hass, mac, connectable=True)
        create_device(bytes.fromhex(adv), ble_device or BLEDevice(mac, None, None))

    # https://developers.home-assistant.io/docs/core/bluetooth/api/
    entry.async_on_unload(
        bluetooth.async_register_callback(
            hass,
            update_ble,
            {"address": entry.data["mac"], "manufacturer_id": 171, "connectable": True},
            bluetooth.BluetoothScanningMode.ACTIVE,
        )
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    # Drop the device too: left in hass.data, a reload found it and never set the
    # platforms up again, while its ping loop kept running next to the new one.
    if device := hass.data[DOMAIN].pop(entry.entry_id, None):
        await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
        await device.client.stop()
    return True
