from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN
from .todo import TodoManager
from .view import TodoApiView

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    manager = TodoManager(hass)
    hass.data[DOMAIN] = manager

    hass.http.register_view(TodoApiView(hass, manager))
    return True