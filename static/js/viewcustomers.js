"use strict";

let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#close-btn");

closeBtn.addEventListener("click", () => {
  sidebar.classList.toggle("close");
});
