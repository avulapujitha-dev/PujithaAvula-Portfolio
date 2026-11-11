// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener("click", function (event) {
        const target = document.querySelector(this.getAttribute("href"));

        if (target) {
            event.preventDefault();
            target.scrollIntoView({
                behavior: "smooth"
            });
        }
    });
});

// Reveal animation
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        }
    });
}, {
    threshold: 0.12
});

document.querySelectorAll(
    ".section, .stats, .project-card, .skill-card, .education-card, .achievement-card"
).forEach(element => {
    element.classList.add("reveal");
    observer.observe(element);
});
const roles = [
    "Software Developer",
    "Salesforce Developer",
    "Java & React Developer",
    "Cloud Security Enthusiast",
    "Problem Solver"
];

let roleIndex = 0;

const roleText = document.getElementById("role-text");

function changeRole() {
    if (!roleText) return;

    roleIndex = (roleIndex + 1) % roles.length;
    roleText.textContent = roles[roleIndex];
}

setInterval(changeRole, 2500);