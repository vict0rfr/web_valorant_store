'use strict';

const log_in = document.querySelector(".log-in");
const close_button = document.querySelector(".close-button");
const body = document.querySelector("body");
const section = document.querySelector("section");
const footer = document.querySelector("footer");

log_in.addEventListener("click", () => {
    document.querySelector(".login_box").style.display = "block";
    body.style.backgroundColor = "#181826";
    section.style.backgroundColor = "#181826";
    footer.style.backgroundColor = "#181826";
});

close_button.addEventListener("click", () => {
    document.querySelector(".login_box").style.display = "none";
    body.style.backgroundColor = "#31304D";
    section.style.backgroundColor = "#B6BBC4";
    footer.style.backgroundColor = "#F0ECE5";
});

