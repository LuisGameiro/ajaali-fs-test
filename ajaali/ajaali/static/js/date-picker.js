function datePicker(date) {
  return {
    date: new Date(date),
    showCalendar: false,
    get formattedDate() {
      return this.date.toLocaleDateString("en-US", {
        weekday: "short",
        day: "numeric",
        month: "short",
      });
    },
    prevDay() {
      if (this.date > new Date()) {
        this.date = new Date(this.date.setDate(this.date.getDate() - 1));
        this.updateFormField();
      }
    },
    nextDay() {
      this.date = new Date(this.date.setDate(this.date.getDate() + 1));
      this.updateFormField();
    },
    toggleCalendar() {
      flatpickr(this.$refs.flatpickr, {
        defaultDate: this.date,
        appendTo: this.$refs.calendar,
        minDate: new Date(),
        onChange: (selectedDates) => {
          this.date = new Date(selectedDates[0]);
        },
        onClose: () => {
          this.showCalendar = false;
        },
      }).open();
    },
    updateFormField() {
      this.$refs.flatpickr.value = this.date.toISOString().split("T")[0];
      if (this.$refs.flatpickr._flatpickr) {
        this.$refs.flatpickr._flatpickr.setDate(this.date, true);
      }
    },
  };
}

document.addEventListener("alpine:init", () => {
  Alpine.data("datePicker", datePicker);
});
