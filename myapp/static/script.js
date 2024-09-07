const tabToggles = document.querySelectorAll(".tabToggle");
const tabContents = document.querySelectorAll(".tabcontent");
tabToggles[0].classList.add("active");
tabContents[0].style.display = "block";

tabToggles.forEach((toggle) => {
  toggle.addEventListener("click", () => {
    const tabId = toggle.getAttribute("data-tab");

    tabToggles.forEach((t) => {
      t.classList.remove("active");
    });

    toggle.classList.add("active");

    tabContents.forEach((content) => {
      content.style.display = "none";
    });

    document.getElementById(tabId).style.display = "block";
  });
});
