(function () {
  document.documentElement.classList.add("js-ready");

  const protectedTerms = [
    "Prof. C. N. R. Rao",
    "Prof. C.\u00a0N.\u00a0R.\u00a0Rao",
    "C. N. R. Rao",
    "D. C. Binwal",
    "Dr. Pratap Vishnoi",
    "JNCASR",
    "MoS\u2082",
    "MoSe\u2082",
    "MoSSe",
    "MoS2-based",
    "Mo-based",
    "Cs\u2082BB\u2032X\u2086",
    "SCXRD",
    "PXRD",
    "UV-Vis",
    "SQUID",
    "VSM",
    "HER",
    "halide double perovskites",
    "single-crystal X-ray diffraction"
  ];

  const escapeRegExp = (value) => value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const termPattern = new RegExp(`(${protectedTerms.map(escapeRegExp).join("|")})`, "g");

  const protectTerms = () => {
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        const parent = node.parentElement;
        if (!parent || !termPattern.test(node.nodeValue)) {
          termPattern.lastIndex = 0;
          return NodeFilter.FILTER_REJECT;
        }
        termPattern.lastIndex = 0;
        if (parent.closest("script, style, textarea, input, .nowrap-term, .nowrap-name, .formula")) {
          return NodeFilter.FILTER_REJECT;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);

    nodes.forEach((node) => {
      const fragment = document.createDocumentFragment();
      let lastIndex = 0;
      const text = node.nodeValue;
      text.replace(termPattern, (match, _term, index) => {
        if (index > lastIndex) fragment.append(document.createTextNode(text.slice(lastIndex, index)));
        const span = document.createElement("span");
        span.className = "nowrap-term";
        span.textContent = match;
        fragment.append(span);
        lastIndex = index + match.length;
        return match;
      });
      if (lastIndex < text.length) fragment.append(document.createTextNode(text.slice(lastIndex)));
      node.parentNode.replaceChild(fragment, node);
    });
  };

  const setupReveal = () => {
    const targets = document.querySelectorAll(".card, .page-hero, .gallery-item, .research-theme, .contact-panel");
    targets.forEach((target) => target.classList.add("reveal-item"));

    if (!("IntersectionObserver" in window) || window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      targets.forEach((target) => target.classList.add("is-visible"));
      return;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });

    targets.forEach((target) => observer.observe(target));
  };

  const setupVideos = () => {
    const videos = Array.from(document.querySelectorAll("video"));
    if (!videos.length) return;

    videos.forEach((video) => {
      video.addEventListener("error", () => {
        const media = video.closest(".research-theme-media");
        if (media) media.classList.add("video-failed");
      });
    });

    if (!("IntersectionObserver" in window) || window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      videos.forEach((video) => video.pause());
      return;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        const video = entry.target;
        if (entry.isIntersecting) {
          video.play().catch(() => {});
        } else {
          video.pause();
        }
      });
    }, { threshold: 0.18 });

    videos.forEach((video) => observer.observe(video));
  };

  const setupImages = () => {
    document.querySelectorAll("img").forEach((img, index) => {
      if (index > 1 && !img.hasAttribute("loading")) img.loading = "lazy";
      if (!img.hasAttribute("decoding")) img.decoding = "async";
    });
  };

  document.addEventListener("DOMContentLoaded", () => {
    protectTerms();
    setupImages();
    setupReveal();
    setupVideos();
  });
})();
