
// Button class "alert-btn"
const btn = document.querySelector(".alert-btn");
btn.addEventListener("click", () => alert("This is a JavaScript programmed alert"));

// Button class "start-btn"
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.querySelector(".start-btn");
  btn.addEventListener("click", () => {
    const paraEl = document.createElement("p");
    const bodyEl = document.querySelector("body");

    bodyEl.appendChild(paraEl);
    paraEl.textContent = "The game has started!!!";
  });
});