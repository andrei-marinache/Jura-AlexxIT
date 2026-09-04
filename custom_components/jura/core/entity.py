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

        # Nu setam entity_id: DOMAIN e "jura", deci ieseau id-uri cu domeniul gresit
        # ("jura.<obiect>" in loc de "binary_sensor.<obiect>" etc.) pe toate cele 7
        # platforme. HA doar avertiza si corecta domeniul, dar din 2027.5.0 va esua.
        # Entitatile existente nu se redenumesc: entity_id-ul vine din entity registry,
        # cautat dupa unique_id (entity_platform.py, "Get entity_id from unique ID
        # registration"), iar unique_id-ul de mai sus ramane neschimbat.

        self.internal_update()

        device.register_update(attr, self.internal_update)

    def internal_update(self):
        pass

    async def async_update(self):
        self.device.client.ping()
