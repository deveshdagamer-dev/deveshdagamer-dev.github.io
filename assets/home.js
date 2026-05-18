(function () {
  var loader = document.querySelector('[data-home-loader]');
  if (!loader) return;

  var video = loader.querySelector('video');
  var skip = loader.querySelector('[data-home-loader-skip]');
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finished = false;
  var loadGuard = window.setTimeout(function () {
    if (!video || video.readyState === 0) finishIntro();
  }, 7000);
  var completionGuard = null;

  function finishIntro() {
    if (finished) return;
    finished = true;
    window.clearTimeout(loadGuard);
    window.clearTimeout(completionGuard);
    loader.classList.add('is-leaving');

    if (video) {
      video.pause();
    }

    window.setTimeout(function () {
      loader.hidden = true;
      loader.remove();
    }, reduceMotion ? 60 : 520);
  }

  if (skip) {
    skip.addEventListener('click', finishIntro);
  }

  if (!video || reduceMotion) {
    finishIntro();
    return;
  }

  function playIntro() {
    window.clearTimeout(loadGuard);
    var durationMs = Number.isFinite(video.duration) && video.duration > 0 ? video.duration * 1000 : 5000;
    completionGuard = window.setTimeout(finishIntro, durationMs + 650);

    var playPromise = video.play();
    if (playPromise && typeof playPromise.catch === 'function') {
      playPromise.catch(function () {
        window.setTimeout(finishIntro, 350);
      });
    }
  }

  video.addEventListener('error', finishIntro, { once: true });
  video.addEventListener('ended', finishIntro, { once: true });
  video.addEventListener('timeupdate', function () {
    if (Number.isFinite(video.duration) && video.duration > 0 && video.currentTime >= video.duration - 0.05) {
      finishIntro();
    }
  });

  if (video.readyState >= 1) {
    playIntro();
  } else {
    video.addEventListener('loadedmetadata', playIntro, { once: true });
  }
}());
