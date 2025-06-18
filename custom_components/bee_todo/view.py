from homeassistant.components.http import HomeAssistantView

class TodoApiView(HomeAssistantView):
    url = "/api/bee_todo"
    name = "api:bee_todo"
    requires_auth = False

    def __init__(self, hass, manager):
        self.hass = hass
        self.manager = manager

    async def get(self, request):
        return self.json(self.manager.list_todos())