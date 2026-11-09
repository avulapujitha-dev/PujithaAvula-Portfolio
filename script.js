// Welcome Message
window.onload = function () {
    console.log("Welcome to Avula Pujitha's Portfolio!");
};

// Smooth Scrolling
document.querySelectorAll('nav a').forEach(function (link) {
    link.addEventListener('click', function (event) {
        const target = document.querySelector(this.getAttribute('href'));

        if (target) {
            event.preventDefault();
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
};

// Contact Message
console.log("Portfolio Website Loaded Successfully!");
