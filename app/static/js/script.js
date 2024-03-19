window.addEventListener("DOMContentLoaded", function () {
  const navBtns = document.querySelectorAll(".nav-btn");
  const accordCards = document.querySelectorAll(".accord-card");

  navBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      navBtns.forEach((siblingBtn) => siblingBtn.classList.remove("active"));
      this.classList.add("active");

      const clickedIndex = [...navBtns].indexOf(this);
      accordCards.forEach((card, index) => {
        card.classList.remove("active");
        if (clickedIndex === index) {
          card.classList.add("active");
        }
      });
    });
  });
});
