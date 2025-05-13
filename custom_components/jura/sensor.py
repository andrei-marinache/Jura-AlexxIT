"""Sensor platform for Jura integration."""

import logging
from datetime import timedelta
from typing import Any
from .core.alert_sensors import ALERT_SENSORS
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.const import STATE_UNKNOWN, STATE_UNAVAILABLE

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval

from .core import DOMAIN
from .core.entity import JuraEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Jura sensor based on a config entry."""
    device = hass.data[DOMAIN][entry.entry_id]

    # Create the total coffees sensor
    entities: list = [JuraTotalCoffeeSensor(device)]

    # Create sensors for each product
    for product in device.products:
        product_name = product["@Name"]
        if product.get("@Active") != "false":
            entities.append(JuraProductCountSensor(device, product_name))

    for maintenance_counter in device.maintenance_counters:
        entities.append(JuraMaintenanceCountersSensor(device, maintenance_counter))

    for maintenance_percent in device.maintenance_percents:
        entities.append(JuraMaintenancePercentsSensor(device, maintenance_percent))

    # Create alert sensors
    entities.append(JuraAlertSensor(device))

    async_add_entities(entities)

    # Set up automatic refresh
    update_interval = hass.data[DOMAIN].get("update_interval", 60)

    async def refresh_statistics(*_):
        """Refresh statistics regularly."""
        try:
            await device.read_statistics()
            await device.read_alerts()
        except Exception as ex:
            # we log as info as this is expected if the device is off
            _LOGGER.info(f"Error refreshing statistics: {ex}")

    # Schedule regular updates
    entry.async_on_unload(
        async_track_time_interval(
            hass, refresh_statistics, timedelta(seconds=update_interval)
        )
    )

    # Do an initial refresh
    hass.async_create_task(refresh_statistics())


class JuraStatisticsSensor(JuraEntity, SensorEntity, RestoreEntity):
    """Base class for Jura statistics sensors."""
    should_poll = False

    async def async_added_to_hass(self):
        """Restore previous state."""
        await super().async_added_to_hass()

        old_state = await self.async_get_last_state()
        if old_state and old_state.state not in (STATE_UNKNOWN, STATE_UNAVAILABLE):
            try:
                self._attr_native_value = int(old_state.state)
                _LOGGER.debug(f"Restored state for {self.entity_id}: {old_state.state}")
            except ValueError:
                _LOGGER.warning(f"Cannot restore state for {self.entity_id}: {old_state.state}")
        else:
            _LOGGER.debug(f"No previous state to restore for {self.entity_id}")

        self.async_write_ha_state()

    def __init__(self, device, attr: str):
        """Initialize the sensor."""
        super().__init__(device, attr)

        # Register for updates on statistics
        device.register_statistics_update(self.internal_update)

    @property
    def native_value(self) -> Any:
        """Return the state of the sensor."""
        return self._attr_native_value

    def _get_value(self) -> Any:
        """Get the value for this sensor from statistics."""
        raise NotImplementedError("Subclasses must implement this method")

    def internal_update(self):
        """Override parent method to ensure statistics are refreshed."""
        _LOGGER.debug(f"Updating sensor {self._attr_name}")
        if self.hass is None:
            return

        new_value = self._get_value()
        _LOGGER.debug(f"Updating sensor {self._attr_name} with value {new_value}")

        if new_value is not None:
            self._attr_native_value = new_value
            self.async_write_ha_state()

class JuraTotalCoffeeSensor(JuraStatisticsSensor):
    """Sensor for total coffee count."""

    _attr_icon = "mdi:coffee"
    _attr_state_class = "total_increasing"
    _attr_native_unit_of_measurement = "products"

    def __init__(self, device):
        """Initialize the sensor."""
        super().__init__(device, "total_product")
        self._attr_name = f"{device.name} Total Products"

    def _get_value(self) -> int:
        """Get the total coffee count."""
        value = self.device.statistics.get("total_products", 0)
        _LOGGER.debug(f"Total coffee value: {value}")
        return value


class JuraProductCountSensor(JuraStatisticsSensor):
    """Sensor for individual product count."""

    _attr_icon = "mdi:coffee-outline"
    _attr_state_class = "total_increasing"
    _attr_native_unit_of_measurement = "products"

    def __init__(self, device, product_name: str):
        """Initialize the sensor."""
        self.product_name = product_name
        attr_name = f"product_{product_name.lower().replace(' ', '_')}"
        super().__init__(device, attr_name)
        self._attr_name = f"{device.name} {product_name}"

    def _get_value(self) -> int:
        """Get the count for this specific product."""
        value = self.device.statistics.get("product_counts", {}).get(
            self.product_name, None
        )
        _LOGGER.debug(f"Product {self.product_name} count: {value}")
        return value


class JuraMaintenanceCountersSensor(JuraStatisticsSensor):
    """Sensor for individual maintenance count."""

    _attr_icon = "mdi:wrench"
    _attr_state_class = "total_increasing"
    _attr_native_unit_of_measurement = "times"

    def __init__(self, device, maintenance_counter: str):
        """Initialize the sensor."""
        self.maintenance_counter = maintenance_counter
        attr_name = f"cleaning_count_{maintenance_counter.lower().replace(' ', '_')}"
        super().__init__(device, attr_name)
        self._attr_name = f"MNT {device.name} {maintenance_counter}"

    def _get_value(self) -> int:
        """Get the count for this specific maintenance."""
        value = self.device.statistics.get("maintenance_counters", {}).get(
            self.maintenance_counter, None
        )
        _LOGGER.debug(f"Maintenance counter {self.maintenance_counter} count: {value}")
        return value

class JuraMaintenancePercentsSensor(JuraStatisticsSensor):
    """Sensor for individual maintenance percents."""

    _attr_icon = "mdi:percent"
    _attr_state_class = "total"
    _attr_native_unit_of_measurement = "%"

    def __init__(self, device, maintenance_percent: str):
        """Initialize the sensor."""
        self.maintenance_percent = maintenance_percent
        attr_name = f"cleaning_percent_{maintenance_percent.lower().replace(' ', '_')}"
        super().__init__(device, attr_name)
        self._attr_name = f"MNT % {device.name} {maintenance_percent} Left"

    def _get_value(self) -> int:
        """Get the value for this specific maintenance percent."""
        value = self.device.statistics.get("maintenance_percents", {}).get(
            self.maintenance_percent, None
        )
        _LOGGER.debug(f"Cleaning percent {self.maintenance_percent} %: {value}")
        return value

class JuraAlertSensor(JuraEntity, SensorEntity, RestoreEntity):
    """Sensor for machine alerts."""

    should_poll = False
    _attr_icon = "mdi:alert"
    _attr_device_class = SensorDeviceClass.ENUM
    _attr_options = ["ok", "alert"]

    def __init__(self, device):
        """Initialize the sensor."""
        self._attr_extra_state_attributes = {"active_alerts": []}

        super().__init__(device, "alerts")
        self._attr_name = f"{device.name} Alerts"
        self._attr_native_value = None
        self._attr_icon = "mdi:alert"
        self._attr_device_class = SensorDeviceClass.ENUM
        self._attr_options = ["ok", "alert"]

        # Register for updates on alerts
        device.register_alert_update(self.internal_update)

    async def async_added_to_hass(self):
        """Restore previous state if available."""
        await super().async_added_to_hass()

        old_state = await self.async_get_last_state()
        if old_state and old_state.state not in (STATE_UNKNOWN, STATE_UNAVAILABLE):
            self._attr_native_value = old_state.state
            _LOGGER.debug(f"Restored alert sensor state for {self.entity_id}: {old_state.state}")
        else:
            _LOGGER.debug(f"No previous alert state to restore for {self.entity_id}")

        self.async_write_ha_state()

    @property
    def native_value(self) -> str:
        """Return the state of the sensor."""
        return self._attr_native_value

    def _get_value(self) -> str:
        """Get the alert status."""
        active_alerts = []
        for bit, name in self.device.active_alerts.items():
            active_alerts.append({"bit": bit, "name": name})
        self._attr_extra_state_attributes["active_alerts"] = active_alerts

        if not active_alerts:
            return "ok"

        # Check if any of the active alerts is PROBLEM type
        for alert in active_alerts:
            alert_name = alert["name"]
            matched_sensor = next(
                (s for s in ALERT_SENSORS if s["name_pattern"].lower() in alert_name.lower()),
                None
            )
            if matched_sensor and matched_sensor.get("device_class") == "problem":
                return "alert"

        return "ok"

    def internal_update(self):
        """Update the sensor state."""
        new_value = self._get_value()
        if new_value != self._attr_native_value:
            _LOGGER.debug(f"Alert sensor {self.entity_id} state changed to: {new_value}")
            self._attr_native_value = new_value
            if self.hass:
                self.async_write_ha_state()
