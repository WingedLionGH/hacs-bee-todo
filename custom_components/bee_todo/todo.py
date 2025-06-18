class TodoManager:
    def __init__(self, hass):
        self.todos = [{"id": 1, "title": "Example Todo", "state": "open"}]

    def list_todos(self):
        return self.todos