import asyncio
import logging
import time
from typing import Callable

from bleak import BLEDevice, BleakClient, BleakError
from bleak_retry_connector import establish_connection

from . import encryption
from enum import Enum

_LOGGER = logging.getLogger(__name__)

ACTIVE_TIME = 120
COMMAND_TIME = 15


class UUIDs(Enum):
    """BLE characteristic UUIDs."""

    # https://github.com/Jutta-Proto/protocol-bt-cpp?tab=readme-ov-file#bluetooth-characteristics
    # Start product
    START_PRODUCT = "5A401525-AB2E-2548-C435-08C300000710"
    # Heartbeat
    P_MODE = "5A401529-AB2E-2548-C435-08C300000710"
    # Statistics command
    STATS_COMMAND = "5A401533-AB2E-2548-C435-08C300000710"
    # Statistics data
    STATS_DATA = "5A401534-AB2E-2548-C435-08C300000710"
    # Status (alerts)
    MACHINE_STATUS = "5a401524-AB2E-2548-C435-08C300000710"
    # Manufacturer data
    MANUFACTURER_DATA = "5a401531-AB2E-2548-C435-08C300000710"

class Client:
    def __init__(self, device: BLEDevice, callback: Callable = None, key: int = None):
        self.device = device
        self.callback = callback
        self.client: BleakClient | None = None
        self.loop = asyncio.get_running_loop()

        self.ping_future: asyncio.Future | None = None
        self.ping_task: asyncio.Task | None = None
        self.ping_time = 0
        self.key = key
        self.send_data = None
        self.send_time = 0
        self.send_uuid = None

    def ping(self):
        self.ping_time = time.time() + ACTIVE_TIME

        if not self.ping_task:
            self.ping_task = self.loop.create_task(self._ping_loop())

    def ping_cancel(self):
        # stop ping time
        self.ping_time = 0

        # cancel ping sleep timer
        if self.ping_future:
            self.ping_future.cancel()

    def send(self, data: bytes, uuid: str = UUIDs.START_PRODUCT.value):
        # if send loop active - we change sending data
        self.send_time = time.time() + COMMAND_TIME
        self.send_data = data
        self.send_uuid = uuid

        # refresh ping time
        self.ping()

        # cancel ping sleep timer
        if self.ping_future:
            self.ping_future.cancel()

    async def _ping_loop(self):
        while time.time() < self.ping_time:
            try:
                self.client = await establish_connection(
                    BleakClient, self.device, self.device.address
                )
                if self.callback:
                    self.callback(True)

                # heartbeat loop
                while time.time() < self.ping_time:
                    if self.send_data:
                        if time.time() < self.send_time:
                            await self.client.write_gatt_char(
                                self.send_uuid,
                                data=encrypt(self.send_data, self.key),
                                response=True,
                            )
                        self.send_data = None

                    # important dummy write to keep the connection
                    # https://github.com/Jutta-Proto/protocol-bt-cpp?tab=readme-ov-file#heartbeat
                    heartbeat = [0x00, 0x7F, 0x80]
                    try:
                        await self.client.write_gatt_char(
                            UUIDs.P_MODE.value,
                            data=encrypt(heartbeat, self.key),
                            response=True,
                        )
                        _LOGGER.debug("heartbeat sent")
                    except Exception as e:
                        # we log as info as this is expected if the device is off
                        _LOGGER.info("heartbeat error", exc_info=e)

                    self.ping_future = self.loop.create_future()
                    # 10 is too late, 9 is ok
                    self.loop.call_later(9, self.ping_future.cancel)
                    try:
                        await self.ping_future
                    except asyncio.CancelledError:
                        pass

                await self.client.disconnect()
            except TimeoutError:
                pass
            except BleakError as e:
                _LOGGER.debug("ping error", exc_info=e)
            except Exception as e:
                _LOGGER.warning("ping error", exc_info=e)
            finally:
                self.client = None
                if self.callback:
                    self.callback(False)
                await asyncio.sleep(1)

        self.ping_task = None

    async def read_data_until_ready(
            self,  characteristic: UUIDs, check_pos: int, check_value_not: int | None = None, max_attempts: int=30
    ) -> bytes | None:
        """ Read data from a characteristic until byte in position 'check_pos' is not 'check_value_not'."""
        if not self.client:
            self.ping()

        attempts=0

        while attempts < max_attempts:
            try:
                # async with asyncio.timeout(2):
                data = await self.client.read_gatt_char(characteristic.value)
                decrypted = encryption.encdec(data, self.key)
                _LOGGER.debug(f"Read data from {characteristic.name} ({characteristic.value}):")
                _LOGGER.debug(f"Encrypted: {' '.join(f'{b:02x}' for b in data)}")
                _LOGGER.debug(f"Decrypted: {' '.join(f'{b:02x}' for b in decrypted)}")
                if (check_value_not is None) or (len(decrypted) > check_pos and decrypted[check_pos] != check_value_not):
                    return decrypted
            except Exception:
                pass
            attempts += 1
            await asyncio.sleep(0.8)

        _LOGGER.debug(f"Device not ready for reading data from characteristic {characteristic.name} ({characteristic.value})")
        return None

    async def write_gatt(self, characteristic: UUIDs, data: bytes, max_attempts: int=30):
        if not self.client:
            self.ping()

        attempts=0

        encrypted=encrypt(bytes(data), self.key)
        while attempts < max_attempts:
            try:
                async with asyncio.timeout(2):
                    await self.client.write_gatt_char(characteristic.value, encrypted, response=True)
                _LOGGER.debug(f"Wrote {' '.join(f'{b:02x}' for b in data)} to {characteristic.name} ({characteristic.value}) (encypted as {' '.join(f'{b:02x}' for b in encrypted)})")
                return None
            except Exception:
                pass
            attempts += 1
            await asyncio.sleep(0.8)

        logging.debug(f"Wrote {data} to GATT characteristic {characteristic}")
        return None

    async def read_statistics_data(self, command_bytes: bytes) -> bytes | None:
        """Read statistics data from the device."""
        _LOGGER.debug("Reading Jura statistics from device...")
        # Request statistics
        await self.write_gatt(characteristic=UUIDs.STATS_COMMAND, data=command_bytes)
        # Wait until statistics are ready
        await self.read_data_until_ready(characteristic=UUIDs.STATS_COMMAND, check_pos=0, check_value_not=0x2a)
        # Read statistics data
        result = await self.read_data_until_ready(characteristic=UUIDs.STATS_DATA, check_pos=0)
        return result

    async def read_machine_status(self, timeout: int = 20, retries: int = 30) -> bytes | None:
        """Read machine status from the device."""
        _LOGGER.debug("Reading Jura machine status (alerts)...")

        # #Get machime model - this will help to get correct alarms
        # result = await self.read_data_until_ready(characteristic=UUIDs.MANUFACTURER_DATA, check_pos=0)
        # await asyncio.sleep(1.5)
        result = await self.read_data_until_ready(characteristic=UUIDs.MACHINE_STATUS, check_pos=0)
        return result

def encrypt(data: bytes | list, key: int) -> bytes:
    data = bytearray(data)
    data[0] = key
    return encryption.encdec(data, key)
