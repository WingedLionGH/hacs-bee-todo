class BeeTodoPanel extends HTMLElement {
  connectedCallback() {
    this.innerHTML = "<h1>Bee Todo</h1><p>JS Panel geladen!</p>";
  }
}
customElements.define("bee-todo-panel", BeeTodoPanel);
document.body.innerHTML = "<bee-todo-panel></bee-todo-panel>";