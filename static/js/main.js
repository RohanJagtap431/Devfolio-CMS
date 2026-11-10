
document.addEventListener("DOMContentLoaded", function () {

    const menuToggle = document.getElementById("menuToggle");
    const navMenu = document.getElementById("navMenu");

    const navLinks = document.querySelectorAll(
        "#navMenu .nav-link, #navMenu .nav-cta"
    );

    // MOBILE MENU
    if (menuToggle && navMenu) {

        menuToggle.addEventListener("click", function () {

            const isOpen = navMenu.classList.toggle("active");

            menuToggle.setAttribute(
                "aria-expanded",
                String(isOpen)
            );
        });

        navLinks.forEach(function (link) {

            link.addEventListener("click", function () {

                navMenu.classList.remove("active");

                menuToggle.setAttribute(
                    "aria-expanded",
                    "false"
                );
            });
        });
    }

    // ACTIVE NAVIGATION
    const sections = document.querySelectorAll(
        "main section[id]"
    );

    function updateActiveLink() {

        // Clear active state on pages without homepage sections
        if (sections.length === 0) {

            navLinks.forEach(function (link) {
                link.classList.remove("active");
                link.removeAttribute("aria-current");
            });

            return;
        }

        let currentSection = "home";

        const scrollPosition = window.scrollY + 180;

        sections.forEach(function (section) {

            if (scrollPosition >= section.offsetTop) {
                currentSection = section.id;
            }

        });

        navLinks.forEach(function (link) {

            const url = new URL(link.href);
            const linkSection = url.hash.replace("#", "");

            const isActive = linkSection === currentSection;

            link.classList.toggle("active", isActive);

            if (isActive) {
                link.setAttribute("aria-current", "location");
            } else {
                link.removeAttribute("aria-current");
            }

        });
    }

    window.addEventListener("scroll", updateActiveLink);
    window.addEventListener("load", updateActiveLink);
    window.addEventListener("hashchange", updateActiveLink);

    updateActiveLink();

    // ESCAPE KEY
    document.addEventListener("keydown", function (event) {

        if (event.key === "Escape" && navMenu && menuToggle) {

            navMenu.classList.remove("active");

            menuToggle.setAttribute(
                "aria-expanded",
                "false"
            );
        }
    });

});
