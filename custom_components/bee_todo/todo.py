import os
import json
from homeassistant.core import HomeAssistant

DATA_FILE = "bee_todo_data.json"

class TodoManager:
    def __init__(self, hass: HomeAssistant):
        self.hass = hass
        self.path = hass.config.path(DATA_FILE)
        self.todos = self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)
        return []

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self.todos, f)

    def list_todos(self):
        return self.todos