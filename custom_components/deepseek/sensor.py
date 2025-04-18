"""Sensor platform for DeepSeek integration."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.entity import DeviceInfo

from .const import DOMAIN

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up DeepSeek sensor based on a config entry."""
    # Currently, we don't set up any sensors.
    # This is a placeholder for future functionality.
    pass

class DeepSeekSensor(SensorEntity):
    """Representation of a DeepSeek Sensor."""

    def __init__(self, entry_id: str, name: str):
        """Initialize the sensor."""
        self._entry_id = entry_id
        self._name = name
        self._state = None

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self) -> StateType:
        """Return the state of the sensor."""
        return self._state

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return f"{self._entry_id}_{self._name}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information about this entity."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry_id)},
            name="DeepSeek AI",
            manufacturer="DeepSeek",
        )