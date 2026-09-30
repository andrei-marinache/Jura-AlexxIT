import re

from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo, Entity

from . import DOMAIN
from .device import Device


def sanitize(entity_id: str) -> str:
    entity_id = re.sub(r"[^0-9a-z_]+", "", entity_id.lower())
    entity_id = re.sub(r"_+", "_", entity_id)
    return entity_id


class JuraEntity(Entity):
    _attr_should_poll = False

    def __init__(self, device: Device, attr: str):
        self.device = device
        self.attr = attr

        self._attr_device_info = DeviceInfo(
            connections={(CONNECTION_NETWORK_MAC, device.mac)},
            identifiers={(DOMAIN, device.mac)},
            manufacturer="Jura",
            model=device.model,
            name=device.name or "Jura",
        )
        self._attr_name = device.name + " " + attr.replace("_", " ").title()
        self._attr_unique_id = device.mac.replace(":", "") + "_" + attr

        # Do not set entity_id: DOMAIN is "jura", so the ids got the wrong domain
        # ("jura.<object>" instead of "binary_sensor.<object>" etc.) on all 7
        # platforms. HA only warned and fixed the domain, but from 2027.5.0 it will fail.
        # Existing entities are not renamed: the entity_id comes from the entity registry,
        # looked up by unique_id (entity_platform.py, "Get entity_id from unique ID
        # registration"), and the unique_id above stays the same.

        self.internal_update()

        device.register_update(attr, self.internal_update)

    def internal_update(self):
        pass

    async def async_update(self):
        self.device.client.ping()
