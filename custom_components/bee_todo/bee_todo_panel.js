class BeeTodoPanel extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `<h1>Bee Todo</h1><div id="todo-list">Loading...</div>`;
    fetch("/api/bee_todo")
      .then(r => r.json())
      .then(data => {
        this.querySelector("#todo-list").innerHTML = data
          .map(t => `<div>${t.title}</div>`).join("");
      })
      .catch(e => console.error(e));
  }
}
customElements.define("bee-todo-panel", BeeTodoPanel);
document.body.innerHTML = "<bee-todo-panel></bee-todo-panel>";
