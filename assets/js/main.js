/* CSA Africa — interaction layer.
   Small, dependency-free, and quiet: every effect is either informative
   (reveal, count-up) or functional (nav, rail, lightbox, video). */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ------------------------------------------------------------ header */
  var header = $('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ------------------------------------------------------------ mobile drawer */
  var burger = $('.burger');
  var drawer = $('.drawer');
  if (burger && drawer) {
    var setDrawer = function (open) {
      burger.setAttribute('aria-expanded', String(open));
      drawer.classList.toggle('is-open', open);
      drawer.setAttribute('aria-hidden', String(!open));
      document.body.classList.toggle('nav-open', open);
    };
    burger.addEventListener('click', function () {
      setDrawer(burger.getAttribute('aria-expanded') !== 'true');
    });
    drawer.addEventListener('click', function (e) {
      if (e.target.closest('a')) setDrawer(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) {
        setDrawer(false);
        burger.focus();
      }
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1230 && drawer.classList.contains('is-open')) setDrawer(false);
    });
  }

  /* ------------------------------------------------------------ nav dropdown
     CSS opens the menu on hover/focus; this keeps aria-expanded honest and
     gives pointer users (and touch) a click target that toggles it. */
  $$('.nav__group').forEach(function (group) {
    var toggle = $('.nav__toggle', group);
    if (!toggle) return;
    var set = function (open) { toggle.setAttribute('aria-expanded', String(open)); };

    group.addEventListener('mouseenter', function () { set(true); });
    group.addEventListener('mouseleave', function () { group.classList.remove('is-open'); set(false); });
    group.addEventListener('focusin', function () { set(true); });
    group.addEventListener('focusout', function () {
      if (!group.contains(document.activeElement)) { group.classList.remove('is-open'); set(false); }
    });
    toggle.addEventListener('click', function () {
      var open = !group.classList.contains('is-open');
      group.classList.toggle('is-open', open);
      set(open);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape' || !group.classList.contains('is-open')) return;
      group.classList.remove('is-open');
      set(false);
      toggle.focus();
    });
  });

  /* ------------------------------------------------------------ scroll reveal */
  var revealables = $$('[data-reveal]');
  if (revealables.length) {
    if (reduced || !('IntersectionObserver' in window)) {
      revealables.forEach(function (el) { el.classList.add('is-in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });

      revealables.forEach(function (el) {
        // stagger siblings that share a parent group
        var group = el.closest('[data-reveal-group]');
        if (group) {
          var sibs = $$('[data-reveal]', group);
          var i = sibs.indexOf(el);
          if (i > -1) el.style.setProperty('--d', Math.min(i, 6) * 70 + 'ms');
        }
        io.observe(el);
      });
    }
  }

  /* ------------------------------------------------------------ count-up stats */
  var counters = $$('[data-count]');
  if (counters.length) {
    var animate = function (el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var prefix = el.getAttribute('data-prefix') || '';
      var suffix = el.getAttribute('data-suffix') || '';
      if (reduced) { el.textContent = prefix + target.toLocaleString() + suffix; return; }
      var dur = 1500;
      var start = null;
      var step = function (t) {
        if (start === null) start = t;
        var p = Math.min((t - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = prefix + Math.round(target * eased).toLocaleString() + suffix;
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };

    if (!('IntersectionObserver' in window)) {
      counters.forEach(animate);
    } else {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          animate(entry.target);
          cio.unobserve(entry.target);
        });
      }, { threshold: 0.4 });
      counters.forEach(function (el) {
        el.textContent = (el.getAttribute('data-prefix') || '') + '0' + (el.getAttribute('data-suffix') || '');
        cio.observe(el);
      });
    }
  }

  /* ------------------------------------------------------------ horizontal rails */
  $$('[data-rail]').forEach(function (rail) {
    var wrap = rail.closest('[data-rail-wrap]') || rail.parentNode;
    var prev = $('[data-rail-prev]', wrap);
    var next = $('[data-rail-next]', wrap);
    if (!prev || !next) return;
    var head = prev.closest('.rail-head');

    // Advance by whole cards, as many as currently fit, so a rail of 22 small
    // portraits doesn't need twenty clicks. Pitch is measured, not assumed,
    // because each rail sets its own column width and gap.
    var pitch = function () {
      var a = rail.children[0], b = rail.children[1];
      if (!a) return rail.clientWidth;
      var w = a.getBoundingClientRect().width;
      return b ? b.getBoundingClientRect().left - a.getBoundingClientRect().left : w;
    };
    var step = function () {
      var p = pitch();
      return Math.max(1, Math.floor(rail.clientWidth / p)) * p;
    };
    var sync = function () {
      var max = rail.scrollWidth - rail.clientWidth;
      prev.disabled = rail.scrollLeft < 8;
      next.disabled = rail.scrollLeft > max - 8;
      // nothing to scroll: retire the whole control row rather than leave a
      // count and two dead buttons promising a swipe that does nothing
      var idle = max < 8;
      if (idle) { prev.disabled = next.disabled = true; }
      if (head) head.hidden = idle;
      else { prev.hidden = next.hidden = idle; }
    };
    prev.addEventListener('click', function () {
      rail.scrollBy({ left: -step(), behavior: reduced ? 'auto' : 'smooth' });
    });
    next.addEventListener('click', function () {
      rail.scrollBy({ left: step(), behavior: reduced ? 'auto' : 'smooth' });
    });
    rail.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
    sync();
  });

  /* ------------------------------------------------------------ youtube facade
     Each poster is a plain link to the video. Where an embed can actually work
     we cancel the navigation and play in place; where it cannot — a file://
     copy, which YouTube rejects with player error 153 because there is no
     referrer to validate — we leave the link alone and it opens YouTube. */
  var canEmbed = location.protocol === 'https:' || location.protocol === 'http:';
  $$('[data-video]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (!canEmbed || e.metaKey || e.ctrlKey || e.shiftKey || e.button > 0) return;
      e.preventDefault();
      var shell = link.parentNode;
      var frame = document.createElement('iframe');
      frame.src = 'https://www.youtube-nocookie.com/embed/' + link.getAttribute('data-video') +
        '?autoplay=1&rel=0&playsinline=1&origin=' + encodeURIComponent(location.origin);
      frame.title = link.getAttribute('data-video-title') || 'CSA Africa video';
      frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      frame.referrerPolicy = 'strict-origin-when-cross-origin';
      frame.allowFullscreen = true;
      shell.appendChild(frame);
      shell.setAttribute('data-playing', 'true');
    });
  });

  /* ------------------------------------------------------------ gallery lightbox */
  var gallery = $('[data-gallery]');
  if (gallery) {
    var shots = $$('button', gallery).map(function (b) {
      var img = $('img', b);
      return { src: b.getAttribute('data-full') || img.src, alt: img.alt };
    });
    var index = 0;

    var box = document.createElement('div');
    box.className = 'lightbox';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-modal', 'true');
    box.setAttribute('aria-label', 'Photo viewer');
    box.innerHTML =
      '<button class="lightbox__btn lightbox__close" type="button" aria-label="Close viewer">' +
      '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 1l14 14M15 1L1 15" stroke="currentColor" stroke-width="1.5" fill="none"/></svg></button>' +
      '<img alt="">' +
      '<div class="lightbox__bar">' +
      '<button class="lightbox__btn" type="button" data-lb="prev" aria-label="Previous photo">' +
      '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M10 2L4 8l6 6" stroke="currentColor" stroke-width="1.5" fill="none"/></svg></button>' +
      '<span data-lb-count></span>' +
      '<button class="lightbox__btn" type="button" data-lb="next" aria-label="Next photo">' +
      '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 2l6 6-6 6" stroke="currentColor" stroke-width="1.5" fill="none"/></svg></button>' +
      '</div>';
    document.body.appendChild(box);

    var lbImg = $('img', box);
    var lbCount = $('[data-lb-count]', box);
    var lastFocus = null;

    var show = function (i) {
      index = (i + shots.length) % shots.length;
      lbImg.src = shots[index].src;
      lbImg.alt = shots[index].alt;
      lbCount.textContent = (index + 1) + ' / ' + shots.length;
    };
    var open = function (i, trigger) {
      lastFocus = trigger || null;
      show(i);
      box.classList.add('is-open');
      document.body.classList.add('nav-open');
      $('.lightbox__close', box).focus();
    };
    var close = function () {
      box.classList.remove('is-open');
      document.body.classList.remove('nav-open');
      lbImg.src = '';
      if (lastFocus) lastFocus.focus();
    };

    $$('button', gallery).forEach(function (b, i) {
      b.addEventListener('click', function () { open(i, b); });
    });
    box.addEventListener('click', function (e) {
      var act = e.target.closest('[data-lb]');
      if (act) { show(index + (act.getAttribute('data-lb') === 'next' ? 1 : -1)); return; }
      if (e.target.closest('.lightbox__close') || e.target === box) close();
    });
    document.addEventListener('keydown', function (e) {
      if (!box.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowRight') show(index + 1);
      if (e.key === 'ArrowLeft') show(index - 1);
    });
  }

  /* ------------------------------------------------------------ mailto forms
     The site is static, so forms compose a pre-filled email to CSA Africa
     rather than silently dropping the message. */
  $$('form[data-mailto]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var to = form.getAttribute('data-mailto');
      var subject = form.getAttribute('data-subject') || 'Website enquiry';
      var lines = [];
      $$('input, textarea', form).forEach(function (f) {
        if (!f.name || f.type === 'submit' || f.type === 'checkbox') return;
        lines.push(f.getAttribute('data-label') || f.name, f.value, '');
      });
      var status = $('[data-form-status]', form);
      window.location.href = 'mailto:' + to +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(lines.join('\n'));
      if (status) status.textContent = 'Opening your email app — if nothing happens, write to ' + to + ' directly.';
    });
  });

  /* ------------------------------------------------------------ hero background film
     The poster is in the HTML and carries the hero on its own, so the film
     layers on top once it is playing. It pauses off-screen and in a hidden tab.

     It used to also skip autoplay when navigator.connection reported a 2g/3g
     effectiveType. That API only exists in Chromium, and Chrome's estimate is
     an observed-latency guess that reads "3g" on plenty of ordinary
     connections — so the film autoplayed in Firefox and Safari (no API, no
     guess) and sat paused in Chrome. Only saveData is honoured now: that one is
     a setting the user deliberately turned on, not a measurement. */
  var film = $('[data-hero-video]');
  var motionBtn = $('[data-hero-motion]');
  if (film && motionBtn) {
    var label = $('[data-hero-motion-label]', motionBtn);
    var conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    var thrifty = !!(conn && conn.saveData);
    var loaded = false;
    var wanted = false;   // has the user (or the default) asked for playback?
    var visible = true;

    var setBtn = function (playing) {
      motionBtn.hidden = false;
      motionBtn.setAttribute('aria-pressed', String(playing));
      label.textContent = playing ? 'Pause background video' : 'Play background video';
    };

    var load = function () {
      if (loaded) return;
      loaded = true;
      var narrow = window.matchMedia('(max-width: 780px)').matches;
      film.src = film.getAttribute(narrow ? 'data-src-sm' : 'data-src-lg');
      film.load();
    };

    var start = function () {
      wanted = true;
      load();
      if (!visible) return;
      var p = film.play();
      if (p && p.catch) p.catch(function () { setBtn(false); armRetry(); });
    };

    // If a browser refuses the first play() anyway, take the next thing the
    // visitor does as the gesture it wanted, once.
    var retryArmed = false;
    var armRetry = function () {
      if (retryArmed) return;
      retryArmed = true;
      var go = function () {
        ['pointerdown', 'keydown', 'touchstart', 'scroll'].forEach(function (e) {
          window.removeEventListener(e, go);
        });
        if (wanted && visible) film.play().catch(function () {});
      };
      ['pointerdown', 'keydown', 'touchstart', 'scroll'].forEach(function (e) {
        window.addEventListener(e, go, { once: true, passive: true });
      });
    };
    var stop = function (byUser) {
      if (byUser) wanted = false;
      film.pause();
    };

    var heroEl = film.closest('.hero');
    film.addEventListener('playing', function () {
      film.classList.add('is-playing');
      if (heroEl) heroEl.classList.add('is-film');   // lets the scrim lighten with it
      setBtn(true);
    });
    film.addEventListener('pause', function () { setBtn(false); });

    motionBtn.addEventListener('click', function () {
      if (motionBtn.getAttribute('aria-pressed') === 'true') stop(true);
      else start();
    });

    // don't burn cycles on a hero nobody is looking at
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        if (!visible) film.pause();
        else if (wanted) start();
      }, { threshold: 0.08 }).observe(film);
    }
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) film.pause();
      else if (wanted && visible) start();
    });

    if (reduced || thrifty) setBtn(false);   // offered, never forced
    else start();
  }

  /* ------------------------------------------------------------ year stamp */
  $$('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
