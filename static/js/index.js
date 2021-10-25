"use strict";

document
  .querySelector(".login-content")
  .addEventListener("click", function openModal() {
    document.querySelector("#login").style.display = "block";
    document.querySelector(".content").style.filter = "blur(3px)";
  });

document
  .querySelector(".close")
  .addEventListener("click", function closeModal() {
    document.getElementById("login").style.display = "none";
    document.querySelector(".content").style.filter = "blur(0px)";
    document.querySelector("#login-component").style.display = "block";
    document.querySelector("#register-component").style.display = "none";
    document.querySelector(".register-success-component").style.display =
      "none";
    document.querySelector(".register-failure-component").style.display =
      "none";
  });

// modal = document.getElementById("login");
// document.onclick = function (event) {
//   if (event.target == modal) {
//   console.log("clicked..");
//   modal.style.display = "none";
//   }
// };

document
  .querySelector(".register")
  .addEventListener("click", function openRegister() {
    document.querySelector("#login-component").style.display = "none";
    document.querySelector("#register-component").style.display = "block";
    document.querySelector(".register-success-component").style.display =
      "none";
  });

document
  .querySelector(".goto-login")
  .addEventListener("click", function openLogin() {
    document.querySelector("#login-component").style.display = "block";
    document.querySelector("#register-component").style.display = "none";
    document.querySelector(".register-success-component").style.display =
      "none";
  });

document
  .querySelector(".success-register")
  .addEventListener("click", function openLogin() {
    document.querySelector("#login-component").style.display = "block";
    document.querySelector("#register-component").style.display = "none";
    document.querySelector(".register-success-component").style.display =
      "none";
  });

document
  .querySelector(".failure-register")
  .addEventListener("click", function openLogin() {
    document.querySelector("#login-component").style.display = "none";
    document.querySelector("#register-component").style.display = "block";
    document.querySelector(".register-failure-component").style.display =
      "none";
  });

document
  .querySelector(".failure-login")
  .addEventListener("click", function openLogin() {
    document.querySelector("#login-component").style.display = "block";
    document.querySelector("#register-component").style.display = "none";
    document.querySelector(".login-failure-component").style.display = "none";
  });
