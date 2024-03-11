document.addEventListener('DOMContentLoaded', () => {
    const navbarToggle = document.querySelector("#navbar-toggle");
    const navbarMenu = document.querySelector("#navbar-menu");
  
    navbarToggle.addEventListener("click", () => {
      const isExpanded = navbarToggle.getAttribute("aria-expanded") === "true";
      navbarToggle.setAttribute("aria-expanded", !isExpanded);
      if (!isExpanded) {
        navbarMenu.style.opacity = 1;
        navbarMenu.style.visibility = "visible";
        navbarMenu.style.display = "block"; 
      } else {
        navbarMenu.style.opacity = 0;
        navbarMenu.style.visibility = "hidden";
        navbarMenu.style.display = "none"; 
      }
    });
  });


