from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN
from .todo import TodoManager
from .view import TodoApiView

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    manager = TodoManager(hass)
    hass.data[DOMAIN] = manager

    hass.http.register_view(TodoApiView(hass, manager))
    
    hass.components.frontend.async_register_built_in_panel(
    component_name="custom",
    sidebar_title="Bee Todo",
    sidebar_icon="mdi:format-list-checkbox",
    frontend_url_path="bee_todo",
    config={"name": "bee_todo_panel"},
    require_admin=False,
    )
    
    return True