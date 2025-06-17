import json
import os
from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import STORAGE_DIR

DATA_FILE = "custom_components/bee_todo/data.json"
ASSIGNEES_FILE = "custom_components/bee_todo/assignees.json"

class TodoManager:
    def __init__(self, hass: HomeAssistant):
        self.hass = hass
        self.data_path = hass.config.path(DATA_FILE)
        self.assignees_path = hass.config.path(ASSIGNEES_FILE)
        self.todos = self._load_json(self.data_path, default=[])
        self.assignees = self._load_json(self.assignees_path, default=[])

    def _load_json(self, path, default):
        if not os.path.exists(path):
            return default
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return default

    def _save_json(self, path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def list_todos(self):
        return self.todos

    def add_todo(self, todo):
        self.todos.append(todo)
        self._save_json(self.data_path, self.todos)

    def update_todo(self, todo_id, updated):
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                self.todos[i] = updated
                break
        self._save_json(self.data_path, self.todos)

    def delete_todo(self, todo_id):
        self.todos = [todo for todo in self.todos if todo["id"] != todo_id]
        self._save_json(self.data_path, self.todos)

    def list_assignees(self):
        return self.assignees

    def add_assignee(self, name):
        if name not in self.assignees:
            self.assignees.append(name)
            self._save_json(self.assignees_path, self.assignees)

    def remove_assignee(self, name):
        if name in self.assignees:
            self.assignees.remove(name)
            self._save_json(self.assignees_path, self.assignees)