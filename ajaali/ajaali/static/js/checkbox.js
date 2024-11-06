function checkbox(initial) {
  return {
    selected: [...initial],
    clearSelection() {
      this.selected = [];
    },
  };
}

document.addEventListener("alpine:init", () => {
  Alpine.data("checkbox", checkbox);
});