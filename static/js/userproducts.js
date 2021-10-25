"use strict";

let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#close-btn");

closeBtn.addEventListener("click", () => {
  sidebar.classList.toggle("close");
});

document
  .querySelector(".add-product-content")
  .addEventListener("click", function openModal() {
    document.querySelector("#add-product").style.display = "block";
    var blurContent = document.querySelectorAll(".content");
    for (let i = 0; i < blurContent.length; i++) {
      blurContent[i].style.filter = "blur(3px)";
    }
  });

document
  .querySelector(".close")
  .addEventListener("click", function closeModal() {
    document.getElementById("add-product").style.display = "none";
    var blurContent = document.querySelectorAll(".content");
    for (let i = 0; i < blurContent.length; i++) {
      blurContent[i].style.filter = "blur(0px)";
    }
  });
