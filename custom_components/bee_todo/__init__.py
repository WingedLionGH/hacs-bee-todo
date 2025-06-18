DOMAIN = "bee_todo"

async def async_setup(hass, config):
    return True

async def async_setup_entry(hass, entry):
    hass.http.register_view(TodoApiView(hass, hass.data[DOMAIN]))

    hass.components.frontend.async_register_built_in_panel(
        component_name="iframe",
        sidebar_title="Bee Todo",
        sidebar_icon="mdi:format-list-checkbox",
        frontend_url_path="bee_todo",
        config={"url": "/local/bee_todo_panel.js"}
    )
    return True
