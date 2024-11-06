function swapLocations(search) {
  return {
    swap() {
      const temp = search.departure;
      search.departure = search.destination;
      search.destination = temp;
    },
  };
}

document.addEventListener("alpine:init", () => {
  Alpine.data("swapLocations", swapLocations);
});