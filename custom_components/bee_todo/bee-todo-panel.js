class TodoPanel extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <style>
        .kanban-column { display: inline-block; vertical-align: top; width: 45%; margin: 10px; padding: 10px; background: #f0f0f0; border-radius: 8px; }
        .todo-item { background: white; padding: 8px; margin: 5px; border-radius: 6px; }
        .calendar-day { border: 1px solid #ccc; padding: 5px; width: 14%; display: inline-block; vertical-align: top; height: 100px; overflow-y: auto; }
      </style>
      <div>
        <h1>Todo List</h1>
        <button onclick="createNewTodo()">Add Todo</button>
        <div id="todo-list"></div>
        <h2>Kanban View</h2>
        <div id="kanban">
          <div class="kanban-column" id="open-column">
            <h3>Open</h3>
          </div>
          <div class="kanban-column" id="complete-column">
            <h3>Complete</h3>
          </div>
        </div>
        <h2>Calendar View</h2>
        <div id="calendar"></div>
      </div>
    `;
    this.loadTodos();
  }

  async loadTodos() {
    const todos = await fetch('/api/bee_todo').then(res => res.json());

    // List View
    document.getElementById("todo-list").innerHTML = todos.map(todo => `
      <div class="todo-item">
        <strong>${todo.title}</strong> - ${todo.state}<br/>
        <small>${todo.due_date}</small><br/>
        Assignee: ${todo.assignee}<br/>
        <button onclick="editTodo('${todo.id}')">Edit</button>
        <button onclick="deleteTodo('${todo.id}')">Delete</button>
      </div>
    `).join("");

    // Kanban View
    const openCol = document.getElementById("open-column");
    const completeCol = document.getElementById("complete-column");
    openCol.innerHTML = "<h3>Open</h3>";
    completeCol.innerHTML = "<h3>Complete</h3>";
    todos.forEach(todo => {
      const div = document.createElement("div");
      div.className = "todo-item";
      div.innerHTML = `<strong>${todo.title}</strong><br/><small>${todo.due_date}</small>`;
      if (todo.state === "open") openCol.appendChild(div);
      else completeCol.appendChild(div);
    });

    // Calendar View
    const calendar = document.getElementById("calendar");
    calendar.innerHTML = "";
    const byDate = {};
    todos.forEach(todo => {
      const date = todo.due_date?.split("T")[0];
      if (!byDate[date]) byDate[date] = [];
      byDate[date].push(todo);
    });
    Object.entries(byDate).forEach(([date, items]) => {
      const div = document.createElement("div");
      div.className = "calendar-day";
      div.innerHTML = `<strong>${date}</strong><br/>` + items.map(t => t.title).join("<br/>");
      calendar.appendChild(div);
    });
  }
}

customElements.define('todo-panel', TodoPanel);