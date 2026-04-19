// ===== PARTICLES =====
tsParticles.load("tsparticles", {
    particles: {
        number: { value: 55, density: { enable: true, area: 900 } },
        color: { value: ["#38bdf8", "#818cf8", "#c084fc"] },
        links: {
            enable: true,
            color: "#1e293b",
            distance: 140,
            opacity: 0.5,
            width: 1
        },
        move: {
            enable: true,
            speed: 0.6,
            outModes: "bounce",
            random: true
        },
        opacity: { value: { min: 0.2, max: 0.6 } },
        size: { value: { min: 1, max: 2.5 } },
        shape: { type: "circle" }
    },
    interactivity: {
        events: {
            onHover: { enable: true, mode: "repulse" },
            onClick: { enable: true, mode: "push" }
        },
        modes: {
            repulse: { distance: 120, duration: 0.4 },
            push: { quantity: 3 }
        }
    },
    background: { color: "transparent" }
});

// ===== NAVBAR SCROLL =====
window.addEventListener("scroll", () => {
    const navbar = document.getElementById("navbar");
    if (navbar) {
        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    }
});

// ===== GSAP SCROLL ANIMATIONS =====
gsap.registerPlugin(ScrollTrigger);

// Animate steps
gsap.utils.toArray(".step").forEach((step, i) => {
    gsap.to(step, {
        opacity: 1,
        y: 0,
        duration: 0.6,
        delay: i * 0.15,
        ease: "power2.out",
        scrollTrigger: {
            trigger: ".steps",
            start: "top 80%"
        }
    });
});

// Animate feature cards
gsap.utils.toArray(".feature-card").forEach((card, i) => {
    gsap.to(card, {
        opacity: 1,
        y: 0,
        duration: 0.5,
        delay: i * 0.08,
        ease: "power2.out",
        scrollTrigger: {
            trigger: ".feature-grid",
            start: "top 80%"
        }
    });
});

// ===== ANIMATED COUNTERS =====
document.querySelectorAll(".counter").forEach(counter => {
    const target = parseInt(counter.dataset.target);
    gsap.to({ val: 0 }, {
        val: target,
        duration: 2.5,
        ease: "power2.out",
        delay: 1.3,
        onUpdate: function () {
            counter.textContent = Math.round(this.targets()[0].val);
        }
    });
});

// ===== SMOOTH SCROLL =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            target.scrollIntoView({ behavior: "smooth" });
        }
    });
});