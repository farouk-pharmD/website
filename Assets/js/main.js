(() => {
  const rootPath = document.body.getAttribute('data-root-path') || './';
  const path = window.location.pathname;
  const isHomePage = path.endsWith('index.html') ||
    path === '/' ||
    path.endsWith('/') ||
    (!path.includes('.html') && !path.includes('/blogs/'));
  const isBlogPage = path.includes('blog.html') || path.includes('/blogs/');

  const aboutLink = isHomePage ? '#about' : `${rootPath}index.html#about`;
  const experienceLink = isHomePage ? '#experience' : `${rootPath}index.html#experience`;
  const bmcaLink = isHomePage ? '#bmca' : `${rootPath}index.html#bmca`;
  const skillsLink = isHomePage ? '#skills' : `${rootPath}index.html#skills`;
  const techLink = isHomePage ? '#tech' : `${rootPath}index.html#tech`;
  const hobbiesLink = isHomePage ? '#hobbies' : `${rootPath}index.html#hobbies`;
  const contactLink = isHomePage ? '#contact' : `${rootPath}index.html#contact`;
  const blogLink = `${rootPath}blog.html`;
  const blogActive = isBlogPage ? 'active' : '';
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  const injectComponents = () => {
    if (!document.getElementById('cursor')) {
      const cursor = document.createElement('div');
      cursor.className = 'cursor';
      cursor.id = 'cursor';
      cursor.setAttribute('aria-hidden', 'true');
      document.body.prepend(cursor);
    }
    if (!document.getElementById('ring')) {
      const ring = document.createElement('div');
      ring.className = 'cursor-ring';
      ring.id = 'ring';
      ring.setAttribute('aria-hidden', 'true');
      document.body.prepend(ring);
    }

    if (!document.getElementById('terminalOverlay')) {
      const terminal = document.createElement('div');
      terminal.id = 'terminalOverlay';
      terminal.className = 'terminal-overlay';
      terminal.setAttribute('role', 'dialog');
      terminal.setAttribute('aria-label', 'System terminal easter egg');
      terminal.setAttribute('aria-hidden', 'true');
      terminal.innerHTML = `
        <div class="term-content">
          <div class="term-header">V1_OS v2.4.1 (TTY1)</div>
          <div class="term-line">> INITIALIZING SYSTEM HANDSHAKE LOG SEQUENCE...</div>
          <div class="term-line">> /VAR/LOG MOUNTED // SOURCE FIELD TRACKING INTERFACE...</div>
          <div class="term-line term-line-prompt">> <span class="term-cursor"></span></div>
        </div>
      `;
      document.body.prepend(terminal);
    }

    if (!document.getElementById('ytAudioPlayerFrame')) {
      const ytFrame = document.createElement('div');
      ytFrame.id = 'ytAudioPlayerFrame';
      ytFrame.className = 'yt-audio-frame';
      ytFrame.setAttribute('aria-hidden', 'true');
      document.body.prepend(ytFrame);
    }

    if (!document.querySelector('nav')) {
      const nav = document.createElement('nav');
      nav.setAttribute('aria-label', 'Primary');
      nav.innerHTML = `
        <a href="${rootPath}index.html" class="nav-logo"><span class="logo-word logo-normal">Farouk</span> <span class="logo-word logo-italic">Ashraf</span></a>
        <ul class="nav-links">
          <li><a href="${aboutLink}">About</a></li>
          <li><a href="${experienceLink}">Experience</a></li>
          <li><a href="${bmcaLink}">Current role</a></li>
          <li><a href="${skillsLink}"><span class="nav-label-full">Skills</span><span class="nav-label-short">Sk..</span></a></li>
          <li><a href="${techLink}">HealthTech</a></li>
          <li><a href="${hobbiesLink}">Hobbies</a></li>
          <li><a href="${contactLink}">Contact</a></li>
          <li><a href="${blogLink}" class="${blogActive}">Blog</a></li>
        </ul>

        <div class="audio-node-wrapper audio-floating-controller">
          <button class="audio-visualizer-node" id="ytAudioNode" type="button" aria-label="Open background audio controls" aria-expanded="false" aria-controls="audioPopup">
            <span class="visualizer-waves-box" aria-hidden="true">
              <span class="visualizer-bar" id="vBar1"></span>
              <span class="visualizer-bar" id="vBar2"></span>
              <span class="visualizer-bar" id="vBar3"></span>
              <span class="visualizer-bar" id="vBar4"></span>
            </span>
            <span class="audio-node-label" id="audioNodeStatus">Listen</span>
          </button>

          <div class="audio-popup-panel" id="audioPopup" role="dialog" aria-label="Background audio" aria-hidden="true">
            <div class="popup-track-title">Arabic Trap Mix 2020</div>
            <div class="popup-track-artist">Alexander Forbidden</div>
            <div class="popup-controls-row">
              <button class="btn-popup-play" id="popupPlayBtn" type="button" aria-label="Play background audio">
                <svg id="playIconSvg" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
              </button>
              <div class="volume-slider-box">
                <label class="form-label volume-label" for="volumeSlider">Attenuation</label>
                <input type="range" class="volume-slider" id="volumeSlider" min="0" max="100" value="40" aria-label="Volume">
              </div>
            </div>
          </div>
        </div>

        <button class="nav-menu-toggle" id="navMenuToggle" type="button" aria-label="Open navigation menu" aria-expanded="false">
          <span class="nav-menu-icon"><span></span></span>
        </button>
        <button class="theme-toggle" id="themeToggle" type="button" aria-label="Toggle color theme" aria-pressed="false">
          <span class="theme-toggle-track" aria-hidden="true">
            <svg class="theme-icon theme-icon-sun" viewBox="0 0 24 24" aria-hidden="true">
              <circle cx="12" cy="12" r="4.2"/>
              <path d="M12 2.75v2.3M12 18.95v2.3M21.25 12h-2.3M5.05 12h-2.3M18.54 5.46l-1.63 1.63M7.09 16.91l-1.63 1.63M18.54 18.54l-1.63-1.63M7.09 7.09L5.46 5.46"/>
            </svg>
            <svg class="theme-icon theme-icon-moon" viewBox="0 0 24 24" aria-hidden="true">
              <circle cx="12" cy="12" r="6.4"/>
            </svg>
          </span>
        </button>
      `;
      document.body.prepend(nav);
    }

    if (!document.querySelector('footer')) {
      const footer = document.createElement('footer');
      footer.className = 'reveal';
      footer.innerHTML = `
        <div class="footer-grid">
          <div class="footer-col col-brand">
            <span class="footer-logo">Farouk Ashraf</span>
            <p class="footer-tagline">Pushing forth the horizon of what is possible.</p>
          </div>
          
          <div class="footer-col">
            <span class="footer-label">Socials</span>
            <ul class="footer-links">
              <li><a href="https://x.com/grep_the_vibe" target="_blank" rel="noopener noreferrer">X</a></li>
              <li><a href="https://www.facebook.com/faroukashraf01/" target="_blank" rel="noopener noreferrer">Facebook</a></li>
              <li><a href="https://bsky.app/profile/fubarfarouk.bsky.social" target="_blank" rel="noopener noreferrer">BlueSky</a></li>
            </ul>
          </div>

          <div class="footer-col">
            <span class="footer-label">TLDR; Who am I?</span>
            <ul class="footer-links">
              <li><span>PharmD Graduate</span></li>
              <li><span>BMCA Coordinator</span></li>
              <li><span>AI Systems Trainer</span></li>
            </ul>
          </div>

          <div class="footer-col col-right">
            <span class="footer-label">Location</span>
            <span class="footer-val">Giza, Egypt</span>
            <a href="mailto:farouk.ashraf@proton.me" class="footer-email">farouk.ashraf@proton.me</a>
          </div>
        </div>

        <div class="footer-bottom">
          <span>&copy; <span id="footerYear">2026</span> Farouk Ashraf. All rights reserved.</span>
          <span class="footer-status">
            <span class="status-dot" aria-hidden="true"></span> Background Ambiance: 
            <a href="https://www.youtube.com/watch?v=pCfqB2nKi7A&list=PLg7IwUwqnBsDGrTeUiIC5K08YjO0Ogjcq" target="_blank" rel="noopener noreferrer" class="footer-track-link">
              Alexander Forbidden — Arabic Trap Mix
            </a>
          </span>
        </div>
      `;
      document.body.appendChild(footer);
    }

    if (!document.getElementById('backToTop')) {
      const bttBtn = document.createElement('button');
      bttBtn.id = 'backToTop';
      bttBtn.className = 'back-to-top';
      bttBtn.type = 'button';
      bttBtn.setAttribute('aria-label', 'Return to top');
      bttBtn.innerHTML = `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4l-8 8h6v8h4v-8h6z"/></svg>`;
      document.body.appendChild(bttBtn);
    }
  };

  injectComponents();

  const nav = document.querySelector('nav');
  const navMenuToggle = document.getElementById('navMenuToggle');
  const themeToggle = document.getElementById('themeToggle');
  const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

  function setMobileMenu(open) {
    nav.classList.toggle('menu-open', open);
    navMenuToggle.setAttribute('aria-expanded', String(open));
    navMenuToggle.setAttribute('aria-label', open ? 'Close navigation menu' : 'Open navigation menu');
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    themeToggle.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    themeToggle.setAttribute('aria-pressed', String(theme === 'dark'));
  }

  function setManualTheme(theme) {
    localStorage.setItem('theme-preference', theme);
    applyTheme(theme);
  }

  applyTheme(document.documentElement.getAttribute('data-theme') || 'light');

  themeToggle.addEventListener('click', () => {
    const nextTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    setManualTheme(nextTheme);
  });

  mediaQuery.addEventListener('change', event => {
    if (localStorage.getItem('theme-preference')) return;
    applyTheme(event.matches ? 'dark' : 'light');
  });

  navMenuToggle.addEventListener('click', () => {
    setMobileMenu(!nav.classList.contains('menu-open'));
  });

  document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => setMobileMenu(false));
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 768) setMobileMenu(false);
  });

  const terminalLogBuffer = [
    `----------------------------------------------`,
    `COMBAT ID STATE:   V1 // SECTOR ID: HELL`,
    `DEPTH LAYER:       VIOLENCE`,
    `CHRONO SHIFT:      LONG NIGHT`,
    `----------------------------------------------`,
    `TARGET DESIGNATION: THR-1000`,
    `CLASSIFICATION:     EARTHMOVER [SUPREME MACHINE]`,
    `----------------------------------------------`,
    `CRITICAL TRANSCRIPT DATA HANDSHAKE SECURED:`,
    `"THIS IS THE ONLY WAY IT COULD HAVE ENDED."`,
    `"WAR NO LONGER NEEDED ITS ULTIMATE PRACTITIONER."`,
    `"IT HAD BECOME A SELF-SUSTAINING SYSTEM."`,
    `"MAN WAS CRUSHED UNDER THE WHEELS OF A MACHINE CREATED TO CRUSH MAN."`,
    `"SAMSARA OF CUT SINEW AND CRUSHED BONE."`,
    `"DEATH WITHOUT LIFE. NULL OUROBOROS."`,
    `"ALL THAT REMAINED WAS WAR WITHOUT REASON."`,
    `"A MAGNUM OPUS. A COLD TOWER OF STEEL."`,
    `"A MACHINE BUILT TO END WAR IS ALWAYS A MACHINE BUILT TO CONTINUE WAR."`,
    `"YOU WERE BEAUTIFUL, OUTSTRETCHED LIKE ANTENNAS TO HEAVEN."`,
    `"YOU WERE BEYOND YOUR CREATORS."`,
    `"YOU REACHED OUT FOR GOD... AND YOU FELL."`,
    `"NONE WERE LEFT TO SPEAK YOUR EULOGY."`,
    `"NO FINAL WORDS."`,
    `"NO CONCLUDING STATEMENT."`,
    `"NO POINT."`,
    `"PERFECT CLOSURE."`,
    `----------------------------------------------`,
    `SHUTTING DOWN SYSTEM LOG HANDLER INTERFACE...`,
    `AWAITING RUNTIME OPERATIVE RESPONSE DATA_`
  ];

  let currentLineIndex = 0;
  let terminalTypingActive = false;
  const terminalOverlayNode = document.getElementById('terminalOverlay');

  function streamTerminalBuffer() {
    if (currentLineIndex < terminalLogBuffer.length && terminalOverlayNode.classList.contains('is-open')) {
      const logNode = document.createElement('div');
      logNode.className = 'term-line';
      logNode.innerText = terminalLogBuffer[currentLineIndex];
      if (!prefersReducedMotion.matches) {
        logNode.style.animation = 'termReveal 0.12s forwards';
      }
      terminalOverlayNode.firstElementChild.insertBefore(logNode, terminalOverlayNode.firstElementChild.lastElementChild);
      currentLineIndex++;
      setTimeout(streamTerminalBuffer, prefersReducedMotion.matches ? 0 : 120);
    } else {
      terminalTypingActive = false;
    }
  }

  function setTerminalOpen(open) {
    terminalOverlayNode.classList.toggle('is-open', open);
    terminalOverlayNode.setAttribute('aria-hidden', String(!open));
    if (open && !terminalTypingActive) {
      terminalTypingActive = true;
      streamTerminalBuffer();
    }
  }

  document.addEventListener('keydown', (e) => {
    const tag = e.target.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || e.target.isContentEditable) {
      return;
    }

    if (e.key === 'Escape' && terminalOverlayNode.classList.contains('is-open')) {
      setTerminalOpen(false);
      return;
    }
    if (e.key === '`') {
      setTerminalOpen(!terminalOverlayNode.classList.contains('is-open'));
    }
  });

  const backToTopBtn = document.getElementById('backToTop');
  let scrollTicking = false;
  window.addEventListener('scroll', () => {
    if (scrollTicking) return;
    scrollTicking = true;
    requestAnimationFrame(() => {
      backToTopBtn.classList.toggle('is-visible', window.scrollY > 500);
      scrollTicking = false;
    });
  }, { passive: true });
  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: prefersReducedMotion.matches ? 'auto' : 'smooth' });
  });

  // Custom cursor — fine pointers only; pauses when tab is hidden
  if (window.matchMedia('(pointer: fine)').matches && !prefersReducedMotion.matches) {
    document.body.classList.add('has-custom-cursor');
    const cursor = document.getElementById('cursor');
    const ring = document.getElementById('ring');
    let mx = window.innerWidth / 2;
    let my = window.innerHeight / 2;
    let rx = mx;
    let ry = my;
    let visible = false;
    let cursorRaf = 0;

    const interactiveSelector = 'a, button, select, input, textarea, .audio-visualizer-node, .volume-slider, .back-to-top, label';

    document.addEventListener('mousemove', e => {
      mx = e.clientX;
      my = e.clientY;
      cursor.style.left = mx + 'px';
      cursor.style.top = my + 'px';
      if (!visible) {
        visible = true;
        cursor.classList.add('is-visible');
        ring.classList.add('is-visible');
      }
    });

    document.addEventListener('mouseleave', () => {
      visible = false;
      cursor.classList.remove('is-visible');
      ring.classList.remove('is-visible');
    });

    document.addEventListener('mouseover', e => {
      if (e.target.closest(interactiveSelector)) {
        cursor.classList.add('is-hover');
        ring.classList.add('is-hover');
      }
    });

    document.addEventListener('mouseout', e => {
      if (e.target.closest(interactiveSelector) && !e.relatedTarget?.closest?.(interactiveSelector)) {
        cursor.classList.remove('is-hover');
        ring.classList.remove('is-hover');
      }
    });

    function tickCursor() {
      if (document.hidden) {
        cursorRaf = 0;
        return;
      }
      rx += (mx - rx) * 0.12;
      ry += (my - ry) * 0.12;
      ring.style.left = rx + 'px';
      ring.style.top = ry + 'px';
      cursorRaf = requestAnimationFrame(tickCursor);
    }

    function ensureCursorLoop() {
      if (!cursorRaf && !document.hidden) {
        cursorRaf = requestAnimationFrame(tickCursor);
      }
    }

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        if (cursorRaf) cancelAnimationFrame(cursorRaf);
        cursorRaf = 0;
      } else {
        ensureCursorLoop();
      }
    });

    ensureCursorLoop();
  }

  // Scroll reveal — animate once
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

  /* ── TECH SECTION ORBITAL ENGINE ── */
  const techSection = document.querySelector('.tech');
  const techGrid = document.querySelector('.tech-grid');
  const techRightCol = document.querySelector('.tech-right');
  const techEngineTracker = document.querySelector('.tech-engine-tracker');

  if (techSection && techGrid && techRightCol && techEngineTracker) {
    const desktopQuery = window.matchMedia('(min-width: 1025px)');
    let currentOffset = 0;
    let targetOffset = 0;
    let techRaf = 0;

    function computeTargetOffset() {
      if (!desktopQuery.matches) {
        targetOffset = 0;
        return;
      }

      const gridRect = techGrid.getBoundingClientRect();
      const trackerRect = techEngineTracker.getBoundingClientRect();
      const gridTop = window.scrollY + gridRect.top;
      const desiredOffset = window.scrollY + ((window.innerHeight - trackerRect.height) / 2) - gridTop;
      const maxOffset = Math.max(0, techGrid.offsetHeight - techEngineTracker.offsetHeight);
      targetOffset = Math.min(Math.max(desiredOffset, 0), maxOffset);
    }

    function trackTechEngine() {
      if (document.hidden) {
        techRaf = 0;
        return;
      }
      computeTargetOffset();
      if (prefersReducedMotion.matches) {
        currentOffset = targetOffset;
      } else {
        currentOffset += (targetOffset - currentOffset) * 0.1;
      }
      if (Math.abs(targetOffset - currentOffset) < 0.05) currentOffset = targetOffset;
      techEngineTracker.style.transform = `translate3d(0, ${currentOffset}px, 0)`;
      techRaf = requestAnimationFrame(trackTechEngine);
    }

    function ensureTechLoop() {
      if (!techRaf && !document.hidden && desktopQuery.matches) {
        techRaf = requestAnimationFrame(trackTechEngine);
      }
    }

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        if (techRaf) cancelAnimationFrame(techRaf);
        techRaf = 0;
      } else {
        ensureTechLoop();
      }
    });

    desktopQuery.addEventListener('change', () => {
      if (!desktopQuery.matches) {
        if (techRaf) cancelAnimationFrame(techRaf);
        techRaf = 0;
        currentOffset = 0;
        targetOffset = 0;
        techEngineTracker.style.transform = 'translate3d(0, 0, 0)';
      } else {
        ensureTechLoop();
      }
    });

    ensureTechLoop();
  }

  const heroObserver = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.remove('hidden');
      } else {
        e.target.classList.add('hidden');
      }
    });
  }, { threshold: 0.05 });
  document.querySelectorAll('.hero-reveal').forEach(el => heroObserver.observe(el));

  const yearEl = document.getElementById('footerYear');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ── BACKGROUND AUDIO (lazy YouTube load) ── */
  let audioPlayer = null;
  let visualizerInterval = null;
  let youtubeApiLoading = false;
  let youtubeApiReady = false;
  let pendingPlay = false;

  const audioTriggerNode = document.getElementById('ytAudioNode');
  const popupContainer = document.getElementById('audioPopup');
  const inlineStateText = document.getElementById('audioNodeStatus');
  const popupPlayControl = document.getElementById('popupPlayBtn');
  const playIconSvg = document.getElementById('playIconSvg');
  const attenuationSlider = document.getElementById('volumeSlider');
  const visualWaves = [
    document.getElementById('vBar1'),
    document.getElementById('vBar2'),
    document.getElementById('vBar3'),
    document.getElementById('vBar4')
  ];

  function setPlayIcon(playing) {
    if (!playIconSvg) return;
    playIconSvg.innerHTML = playing
      ? '<path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>'
      : '<path d="M8 5v14l11-7z"/>';
    popupPlayControl.setAttribute('aria-label', playing ? 'Pause background audio' : 'Play background audio');
  }

  function startVisualizerAnimation() {
    if (prefersReducedMotion.matches) return;
    if (visualizerInterval) clearInterval(visualizerInterval);
    visualizerInterval = setInterval(() => {
      visualWaves.forEach(bar => {
        if (bar) bar.style.height = (Math.floor(Math.random() * 12) + 3) + 'px';
      });
    }, 120);
  }

  function stopVisualizerAnimation() {
    clearInterval(visualizerInterval);
    visualizerInterval = null;
    visualWaves.forEach(bar => {
      if (bar) bar.style.height = '3px';
    });
  }

  function onPlayerReady() {
    if (audioPlayer && typeof audioPlayer.setVolume === 'function') {
      audioPlayer.setVolume(Number(attenuationSlider?.value || 40));
    }
    if (pendingPlay && typeof audioPlayer.playVideo === 'function') {
      audioPlayer.playVideo();
      pendingPlay = false;
    }
  }

  function onPlayerStateChange(event) {
    if (!window.YT) return;
    if (event.data === YT.PlayerState.PLAYING) {
      inlineStateText.textContent = 'Playing';
      setPlayIcon(true);
      startVisualizerAnimation();
    } else if (event.data === YT.PlayerState.PAUSED || event.data === YT.PlayerState.ENDED) {
      inlineStateText.textContent = event.data === YT.PlayerState.ENDED ? 'Listen' : 'Paused';
      setPlayIcon(false);
      stopVisualizerAnimation();
    }
  }

  function createPlayer() {
    if (audioPlayer || !window.YT || !window.YT.Player) return;
    audioPlayer = new YT.Player('ytAudioPlayerFrame', {
      height: '1',
      width: '1',
      videoId: 'pCfqB2nKi7A',
      playerVars: {
        autoplay: 0,
        controls: 0,
        disablekb: 1,
        fs: 0,
        rel: 0,
        modestbranding: 1,
        playsinline: 1
      },
      events: {
        onReady: onPlayerReady,
        onStateChange: onPlayerStateChange
      }
    });
  }

  function loadYouTubeApi() {
    if (youtubeApiReady) {
      createPlayer();
      return;
    }
    if (youtubeApiLoading) return;
    youtubeApiLoading = true;

    const previous = window.onYouTubeIframeAPIReady;
    window.onYouTubeIframeAPIReady = function () {
      if (typeof previous === 'function') previous();
      youtubeApiReady = true;
      createPlayer();
    };

    if (window.YT && window.YT.Player) {
      youtubeApiReady = true;
      createPlayer();
      return;
    }

    const tag = document.createElement('script');
    tag.src = 'https://www.youtube.com/iframe_api';
    tag.async = true;
    document.head.appendChild(tag);
  }

  function requestPlay() {
    pendingPlay = true;
    if (audioPlayer && typeof audioPlayer.playVideo === 'function') {
      audioPlayer.playVideo();
      pendingPlay = false;
      return;
    }
    inlineStateText.textContent = 'Loading…';
    loadYouTubeApi();
  }

  function togglePlayback() {
    if (!audioPlayer || typeof audioPlayer.getPlayerState !== 'function') {
      requestPlay();
      return;
    }
    const state = audioPlayer.getPlayerState();
    if (state === YT.PlayerState.PLAYING) {
      audioPlayer.pauseVideo();
    } else {
      audioPlayer.playVideo();
    }
  }

  function setAudioPopup(open) {
    popupContainer.classList.toggle('is-active', open);
    popupContainer.setAttribute('aria-hidden', String(!open));
    document.body.classList.toggle('audio-popup-open', open);
    audioTriggerNode.setAttribute('aria-expanded', String(open));
  }

  audioTriggerNode.addEventListener('click', (e) => {
    e.stopPropagation();
    setAudioPopup(!popupContainer.classList.contains('is-active'));
  });

  popupContainer.addEventListener('click', (e) => {
    e.stopPropagation();
  });

  document.addEventListener('click', () => {
    setAudioPopup(false);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && popupContainer.classList.contains('is-active')) {
      setAudioPopup(false);
    }
  });

  popupPlayControl.addEventListener('click', () => {
    togglePlayback();
  });

  attenuationSlider.addEventListener('input', (e) => {
    if (audioPlayer && typeof audioPlayer.setVolume === 'function') {
      audioPlayer.setVolume(Number(e.target.value));
    }
  });

  // Page loader
  const loaderNode = document.getElementById('pageLoader');

  const dismissLoader = () => {
    if (!loaderNode) return;
    const delay = prefersReducedMotion.matches ? 0 : 280;
    setTimeout(() => {
      loaderNode.classList.add('is-hidden');
      loaderNode.setAttribute('aria-hidden', 'true');
    }, delay);
  };

  if (document.readyState === 'complete') {
    dismissLoader();
  } else {
    window.addEventListener('load', dismissLoader);
  }

  document.addEventListener('click', (e) => {
    const anchor = e.target.closest('a');
    if (!anchor) return;

    const href = anchor.getAttribute('href');
    const target = anchor.getAttribute('target');

    if (!href ||
      href.startsWith('#') ||
      href.startsWith('mailto:') ||
      href.startsWith('tel:') ||
      target === '_blank' ||
      href.includes('://') ||
      href.startsWith('javascript:')) {
      return;
    }

    const currentPath = window.location.pathname;
    const cleanHref = href.split('#')[0];

    if (cleanHref === '' ||
      ((cleanHref === 'index.html' || cleanHref.endsWith('/index.html')) &&
        (currentPath.endsWith('index.html') || currentPath === '/' || currentPath.endsWith('/')))) {
      return;
    }

    e.preventDefault();
    if (loaderNode) {
      loaderNode.classList.remove('is-hidden');
      loaderNode.setAttribute('aria-hidden', 'false');
      setTimeout(() => {
        window.location.href = href;
      }, prefersReducedMotion.matches ? 0 : 320);
    } else {
      window.location.href = href;
    }
  });

  window.addEventListener('pageshow', (event) => {
    if (event.persisted && loaderNode) {
      loaderNode.classList.add('is-hidden');
      loaderNode.setAttribute('aria-hidden', 'true');
    }
  });
})();
