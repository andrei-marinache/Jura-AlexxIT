import logging
from .core.alert_sensors import ALERT_SENSORS

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.const import STATE_ON, STATE_OFF, STATE_UNKNOWN, STATE_UNAVAILABLE

from . import DOMAIN
from .core.entity import JuraEntity

_LOGGER = logging.getLogger(__name__)

# Define alert sensors with their expected alert names and configurations


async def async_setup_entry(
    hass: HomeAssistant, config_entry: ConfigEntry, add_entities: AddEntitiesCallback
):
    device = hass.data[DOMAIN][config_entry.entry_id]

    # Create connection sensor
    entities: list = [JuraSensor(device, "connection")]

    # Create alert binary sensors if they are defined for this device
    for alert_info in ALERT_SENSORS:
        for alert in device.alerts.values():
            if alert == alert_info['name_pattern']:
                entities.append(JuraAlertBinarySensor(device, alert_info))
    add_entities(entities)


class JuraSensor(JuraEntity, BinarySensorEntity):
    _attr_device_class = "connectivity"
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def internal_update(self):
        self._attr_is_on = self.device.connected
        self._attr_extra_state_attributes = self.device.conn_info

        if self.hass:
            self._async_write_ha_state()


class JuraAlertBinarySensor(JuraEntity, BinarySensorEntity, RestoreEntity):
    """Binary sensor for Jura alerts."""

    should_poll = False

    def __init__(self, device, alert_info: dict):
        """Initialize the sensor."""
        # Store name pattern before calling super().__init__
        self._name_pattern = alert_info["name_pattern"].lower()

        super().__init__(device, f"alert_{alert_info['type']}")

        self._attr_name = f"{device.name} {alert_info['display_name']}"

        if "icon" in alert_info:
            self._attr_icon = alert_info["icon"]
        self._attr_device_class = alert_info["device_class"]
        self._attr_entity_category = alert_info["entity_category"]

        # Register for updates on alerts
        device.register_alert_update(self.internal_update)

    async def async_added_to_hass(self):
        """Restore previous state if available."""
        await super().async_added_to_hass()

        old_state = await self.async_get_last_state()
        if old_state and old_state.state not in (STATE_UNKNOWN, STATE_UNAVAILABLE):
            self._attr_is_on = old_state.state == STATE_ON
            _LOGGER.debug(f"Restored state for {self.entity_id}: {old_state.state}")
        else:
            _LOGGER.debug(f"No previous state to restore for {self.entity_id}")

        self.async_write_ha_state()

    def internal_update(self):
        """Update the sensor state."""
        # Check if any active alert's name contains our pattern
        is_active = any(
            self._name_pattern in alert_name.lower()
            for _, alert_name in self.device.active_alerts.items()
        )

        if is_active != self._attr_is_on:
            _LOGGER.debug(f"Alert state for {self.entity_id} changed to: {is_active}")
            self._attr_is_on = is_active
            if self.hass:
                self._async_write_ha_state()