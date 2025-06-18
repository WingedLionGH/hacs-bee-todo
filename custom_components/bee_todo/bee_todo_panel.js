class BeeTodoPanel extends HTMLElement {
  connectedCallback() {
    this.innerHTML = \`
      <style>
        .todo-box { padding: 16px; font-family: sans-serif; }
        .todo-item { background: #eee; padding: 8px; margin: 6px 0; border-radius: 5px; }
      </style>
      <div class="todo-box">
        <h1>Bee Todo</h1>
        <div id="todo-list">Loading...</div>
      </div>
    \`;
    this.loadTodos();
  }

  async loadTodos() {
    try {
      const response = await fetch('/api/bee_todo');
      const todos = await response.json();
      const container = this.querySelector("#todo-list");
      container.innerHTML = todos.map(todo => \`
        <div class="todo-item"><strong>\${todo.title}</strong></div>
      \`).join("");
    } catch (e) {
      console.error("Failed to load todos:", e);
    }
  }
}

customElements.define('bee-todo-panel', BeeTodoPanel);
document.body.innerHTML = "<bee-todo-panel></bee-todo-panel>";