// menu toggle
var navLinks = document.getElementById("navLinks")

function hideMenu() {
    navLinks.style.right = "-200px";
}

function showMenu() {
    navLinks.style.right = "0";
}

// To toggle User

let subMenu = document.getElementById('subMenu')

function toggleUser() {
    subMenu.classList.toggle("open-menu");
}
