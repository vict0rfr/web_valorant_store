"use strict";

const log_in = document.querySelector(".log-in");
const close_button = document.querySelector(".close-button");
const body = document.querySelector("body");
const section = document.querySelector("section");
const footer = document.querySelector("footer");
const bundleOfferImage = document.querySelector("#bundleImg");
const timeElement = document.querySelector(".time-left");

log_in.addEventListener("click", () => {
    document.querySelector(".login_box").style.display = "block";
    body.style.backgroundColor = "#181826";
    section.style.backgroundColor = "#181826";
    footer.style.backgroundColor = "#181826";
    document.querySelectorAll("div.grid > article > figure > img").forEach((img) => {
      img.style.opacity = "0.4";
    });
    bundleOfferImage.style.opacity = "0.4";
});

  
close_button.addEventListener("click", () => {
  document.querySelector(".login_box").style.display = "none";
  body.style.backgroundColor = "#31304D";
  section.style.backgroundColor = "#B6BBC4";
  footer.style.backgroundColor = "#F0ECE5";
  document.querySelectorAll("div.grid > article > figure > img").forEach((img) => {
      img.style.opacity = "1";
    });
  bundleOfferImage.style.opacity = "1";
});
if (window.location.pathname === "/itemshop.html") {
  let tempCountdown = timeElement.innerText;
  let temp = tempCountdown;

  let hours = Math.floor((temp % (60 * 60 * 24)) / (60 * 60)).toString();
  let minutes = Math.floor((temp % (60 * 60)) / 60).toString();
  let seconds = Math.floor(temp % 60).toString();

  timeElement.innerText = hours + "h" + minutes + "m" + seconds + "s";

  var x = setInterval(function () {
    let distance = (tempCountdown -= 1);

    let hours = Math.floor((distance % (60 * 60 * 24)) / (60 * 60)).toString();
    let minutes = Math.floor((distance % (60 * 60)) / 60).toString();
    let seconds = Math.floor(distance % 60).toString();

    timeElement.innerText = hours + "h" + minutes + "m" + seconds + "s";
  }, 1000);
}

function visibility() {
  const button = document.querySelector("body > div > div.login_form > form > div > span > button")
  const password = document.querySelector("body > div > div.login_form > form > div > input");
  if (button.innerText === "visibility_off") {
    button.innerText = "visibility";
    password.type = "text";
  } else {
    button.innerText = "visibility_off";
    password.type = "password";
  }
}