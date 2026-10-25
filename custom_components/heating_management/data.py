"""Custom types for heating_management."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import HeatingManagementApiClient
    from .coordinator import HeatingManagementCoordinator


type HeatingManagementConfigEntry = ConfigEntry[HeatingManagementData]


@dataclass
class HeatingManagementData:
    """Data for the Heating Management integration."""

    client: HeatingManagementApiClient
    coordinator: HeatingManagementCoordinator
    integration: Integration
