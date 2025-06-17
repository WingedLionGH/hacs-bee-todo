from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from homeassistant.components.http import HomeAssistantView
import os
import json

from .todo import TodoManager


class TodoApiView(HomeAssistantView):
    url = "/api/bee_todo"
    name = "api:bee_todo"
    requires_auth = False

    def __init__(self, hass: HomeAssistant, manager: TodoManager):
        self.hass = hass
        self.manager = manager

    async def get(self, request):
        return self.json(self.manager.list_todos())


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    manager = TodoManager(hass)
    hass.data["bee_todo"] = manager

    # Register API view
    hass.http.register_view(TodoApiView(hass, manager))

    # Register custom panel
    panel_path = hass.config.path("custom_components/bee_todo/frontend")
    hass.components.frontend.async_register_built_in_panel(
        component_name="iframe",
        sidebar_title="HACS Todo",
        sidebar_icon="mdi:format-list-checkbox",
        frontend_url_path="bee_todo",
        config={
            "url": "/local/bee_todo_panel.html"
        },
        require_admin=False
    )

    return True