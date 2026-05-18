(function () {
  const prefersReducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const setupIntro = () => {
    const intro = document.querySelector("[data-gallery-intro]");
    if (!intro) return;

    const skip = intro.querySelector("[data-gallery-intro-skip]");
    let finished = false;
    const timer = window.setTimeout(finishIntro, prefersReducedMotion ? 250 : 4700);

    function finishIntro() {
      if (finished) return;
      finished = true;
      window.clearTimeout(timer);
      intro.classList.add("is-leaving");
      window.setTimeout(() => intro.remove(), prefersReducedMotion ? 80 : 520);
    }

    if (skip) skip.addEventListener("click", finishIntro);
    if (prefersReducedMotion) finishIntro();
  };

  const setupLightbox = () => {
    const figures = Array.from(document.querySelectorAll(".gallery-item, .carousel-slide"));
    if (!figures.length) return;

    const lightbox = document.createElement("div");
    lightbox.className = "gallery-lightbox";
    lightbox.hidden = true;
    lightbox.innerHTML = [
      '<button class="gallery-lightbox-close" type="button" aria-label="Close preview">Close</button>',
      '<img class="gallery-lightbox-image" alt="">',
      '<p class="gallery-lightbox-caption"></p>'
    ].join("");
    document.body.append(lightbox);

    const image = lightbox.querySelector(".gallery-lightbox-image");
    const caption = lightbox.querySelector(".gallery-lightbox-caption");
    const close = lightbox.querySelector(".gallery-lightbox-close");

    const openPreview = (img, text) => {
      image.src = img.currentSrc || img.src;
      image.alt = img.alt || text || "Gallery image";
      caption.textContent = text || img.alt || "";
      lightbox.hidden = false;
      lightbox.classList.add("is-open");
      document.documentElement.classList.add("lightbox-open");
      close.focus({ preventScroll: true });
    };

    const closePreview = () => {
      lightbox.classList.remove("is-open");
      lightbox.hidden = true;
      image.removeAttribute("src");
      document.documentElement.classList.remove("lightbox-open");
    };

    figures.forEach((figure) => {
      const img = figure.querySelector("img");
      if (!img) return;
      const captionText = figure.querySelector("figcaption")?.textContent.trim() || img.alt;
      img.tabIndex = 0;
      img.setAttribute("role", "button");
      img.setAttribute("aria-label", `Open larger preview: ${img.alt || captionText || "gallery image"}`);
      img.addEventListener("click", () => openPreview(img, captionText));
      img.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          openPreview(img, captionText);
        }
      });
    });

    close.addEventListener("click", closePreview);
    lightbox.addEventListener("click", (event) => {
      if (event.target === lightbox) closePreview();
    });
    document.addEventListener("keydown", (event) => {
      if (!lightbox.hidden && event.key === "Escape") closePreview();
    });
  };

  document.addEventListener("DOMContentLoaded", () => {
    setupIntro();
    setupLightbox();
  });
}());
