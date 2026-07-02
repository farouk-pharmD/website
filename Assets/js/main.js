(() => {
  // Determine root path prefix and page info
  const rootPath = document.body.getAttribute('data-root-path') || './';
  const isHomePage = window.location.pathname.endsWith('index.html') ||
    window.location.pathname === '/' ||
    window.location.pathname.endsWith('/') ||
    (!window.location.pathname.includes('.html') && !window.location.pathname.includes('/blogs/'));
  const isBlogPage = window.location.pathname.includes('blog.html') || window.location.pathname.includes('/blogs/');

  // Generate dynamic links depending on where the user is
  const aboutLink = isHomePage ? '#about' : `${rootPath}index.html#about`;
  const experienceLink = isHomePage ? '#experience' : `${rootPath}index.html#experience`;
  const bmcaLink = isHomePage ? '#bmca' : `${rootPath}index.html#bmca`;
  const skillsLink = isHomePage ? '#skills' : `${rootPath}index.html#skills`;
  const techLink = isHomePage ? '#tech' : `${rootPath}index.html#tech`;
  const hobbiesLink = isHomePage ? '#hobbies' : `${rootPath}index.html#hobbies`;
  const contactLink = isHomePage ? '#contact' : `${rootPath}index.html#contact`;
  const blogLink = `${rootPath}blog.html`;
  const blogActive = isBlogPage ? 'active' : '';

  // 1. Inject Shared HTML Structure
  const injectComponents = () => {
    // Prepend Cursor Custom Elements
    if (!document.getElementById('cursor')) {
      const cursor = document.createElement('div');
      cursor.className = 'cursor';
      cursor.id = 'cursor';
      document.body.prepend(cursor);
    }
    if (!document.getElementById('ring')) {
      const ring = document.createElement('div');
      ring.className = 'cursor-ring';
      ring.id = 'ring';
      document.body.prepend(ring);
    }

    // Prepend Terminal Overlay
    if (!document.getElementById('terminalOverlay')) {
      const terminal = document.createElement('div');
      terminal.id = 'terminalOverlay';
      terminal.className = 'terminal-overlay';
      terminal.innerHTML = `
        <div class="term-content">
          <div class="term-header">V1_OS v2.4.1 (TTY1)</div>
          <div class="term-line">> INITIALIZING SYSTEM HANDSHAKE LOG SEQUENCE...</div>
          <div class="term-line">> /VAR/LOG MOUNTED // SOURCE FIELD TRACKING INTERFACE...</div>
          <div class="term-line" style="margin-top: 1.5rem;">> <span class="term-cursor"></span></div>
        </div>
      `;
      document.body.prepend(terminal);
    }

    // Prepend Hidden YouTube audio target frame
    if (!document.getElementById('ytAudioPlayerFrame')) {
      const ytFrame = document.createElement('div');
      ytFrame.id = 'ytAudioPlayerFrame';
      ytFrame.style = 'position:absolute; width:1px; height:1px; opacity:0; pointer-events:none; overflow:hidden; left:-9999px; top:-9999px;';
      document.body.prepend(ytFrame);
    }

    // Prepend Navigation Bar
    if (!document.querySelector('nav')) {
      const nav = document.createElement('nav');
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

        <!-- Persistent Asymmetric Rhythmic Audio Dropdown Wrapper -->
        <div class="audio-node-wrapper audio-floating-controller">
          <button class="audio-visualizer-node" id="ytAudioNode" type="button" aria-label="Toggle structural background stream">
            <span class="visualizer-waves-box">
              <span class="visualizer-bar" id="vBar1"></span>
              <span class="visualizer-bar" id="vBar2"></span>
              <span class="visualizer-bar" id="vBar3"></span>
              <span class="visualizer-bar" id="vBar4"></span>
            </span>
            <span class="audio-node-label" id="audioNodeStatus">Listen</span>
          </button>

          <!-- Glassmorphism Dropdown Interface Panel -->
          <div class="audio-popup-panel" id="audioPopup">
            <div class="popup-track-title">Arabic Trap Mix 2020</div>
            <div class="popup-track-artist">Alexander Forbidden</div>
            <div class="popup-controls-row">
              <button class="btn-popup-play" id="popupPlayBtn" aria-label="Toggle audio playback">
                <svg id="playIconSvg" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </button>
              <div class="volume-slider-box">
                <span class="form-label" style="font-size:0.5rem; letter-spacing:0.1em;">Attenuation</span>
                <input type="range" class="volume-slider" id="volumeSlider" min="0" max="100" value="40" aria-label="Volume controller">
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

    // Append Editorial Footer
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
              <li><a href="https://x.com/grep_the_vibe" target="_blank">X</a></li>
              <li><a href="https://www.facebook.com/faroukashraf01/" target="_blank">Facebook</a></li>
              <li><a href="https://bsky.app/profile/fubarfarouk.bsky.social" target="_blank">BlueSky</a></li>
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
            <span class="status-dot"></span> Background Ambiance: 
            <a href="https://www.youtube.com/watch?v=pCfqB2nKi7A&list=PLg7IwUwqnBsDGrTeUiIC5K08YjO0Ogjcq" target="_blank" style="text-decoration: underline; color: inherit; font-size: inherit; margin-left: 2px;">
              Alexander Forbidden — Arabic Trap Mix
            </a>
          </span>
        </div>
      `;
      document.body.appendChild(footer);
    }

    // Append Back to Top Button
    if (!document.getElementById('backToTop')) {
      const bttBtn = document.createElement('button');
      bttBtn.id = 'backToTop';
      bttBtn.className = 'back-to-top';
      bttBtn.setAttribute('aria-label', 'Return to top');
      bttBtn.innerHTML = `<svg viewBox="0 0 24 24"><path d="M12 4l-8 8h6v8h4v-8h6z"/></svg>`;
      document.body.appendChild(bttBtn);
    }
  };

  injectComponents();

  // 2. Initialize Interactive Elements and Event Handlers
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

  // Terminal Easter Egg DATA STORAGE ARRAY & LOGIC
  const terminal_Log_Buffer = [
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
    if (currentLineIndex < terminal_Log_Buffer.length && terminalOverlayNode.classList.contains('is-open')) {
      const logNode = document.createElement('div');
      logNode.className = 'term-line';
      logNode.innerText = terminal_Log_Buffer[currentLineIndex];
      logNode.style.animation = 'termReveal 0.12s forwards';

      terminalOverlayNode.firstElementChild.insertBefore(logNode, terminalOverlayNode.firstElementChild.lastElementChild);

      currentLineIndex++;
      setTimeout(streamTerminalBuffer, 120);
    } else {
      terminalTypingActive = false;
    }
  }

  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') {
      return;
    }

    if (e.key === '`') {
      if (!terminalOverlayNode.classList.contains('is-open')) {
        terminalOverlayNode.classList.add('is-open');
        if (!terminalTypingActive) {
          terminalTypingActive = true;
          streamTerminalBuffer();
        }
      } else {
        terminalOverlayNode.classList.remove('is-open');
      }
    }
  });

  // Back to Top Button Logic
  const backToTopBtn = document.getElementById('backToTop');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
      backToTopBtn.classList.add('is-visible');
    } else {
      backToTopBtn.classList.remove('is-visible');
    }
  });
  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // Custom cursor setup
  if (window.matchMedia('(pointer: fine)').matches) {
    document.body.classList.add('has-custom-cursor');
    const cursor = document.getElementById('cursor');
    const ring = document.getElementById('ring');
    let mx = window.innerWidth / 2, my = window.innerHeight / 2;
    let rx = mx, ry = my;
    let visible = false;

    document.addEventListener('mousemove', e => {
      mx = e.clientX; my = e.clientY;
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

    (function tick() {
      rx += (mx - rx) * 0.12;
      ry += (my - ry) * 0.12;
      ring.style.left = rx + 'px';
      ring.style.top = ry + 'px';
      requestAnimationFrame(tick);
    })();

    const updateCursorHoverBindings = () => {
      document.querySelectorAll('a, button, select, input, .audio-visualizer-node, .volume-slider, .back-to-top').forEach(el => {
        // Remove existing to avoid duplicates
        el.removeEventListener('mouseenter', growCursor);
        el.removeEventListener('mouseleave', shrinkCursor);

        el.addEventListener('mouseenter', growCursor);
        el.addEventListener('mouseleave', shrinkCursor);
      });
    };

    function growCursor() {
      cursor.style.width = cursor.style.height = '18px';
      ring.style.width = ring.style.height = '54px';
    }

    function shrinkCursor() {
      cursor.style.width = cursor.style.height = '10px';
      ring.style.width = ring.style.height = '36px';
    }

    updateCursorHoverBindings();

    // MutationObserver to bind dynamically added elements in future
    const observer = new MutationObserver(updateCursorHoverBindings);
    observer.observe(document.body, { childList: true, subtree: true });
  }

  // Scroll reveal tracking configuration
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
      } else {
        e.target.classList.remove('visible');
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
  /* ── TECH SECTION ORBITAL ENGINE SCROLL TRACKING ── */
  const techSection = document.querySelector('.tech');
  const techGrid = document.querySelector('.tech-grid');
  const techRightCol = document.querySelector('.tech-right');
  const techEngineTracker = document.querySelector('.tech-engine-tracker');

  if (techSection && techGrid && techRightCol && techEngineTracker) {
    const desktopQuery = window.matchMedia('(min-width: 1025px)');
    const reducedMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    let currentOffset = 0;
    let targetOffset = 0;

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
      computeTargetOffset();
      if (reducedMotionQuery.matches) {
        currentOffset = targetOffset;
      } else {
        currentOffset += (targetOffset - currentOffset) * 0.1;
      }
      if (Math.abs(targetOffset - currentOffset) < 0.05) currentOffset = targetOffset;
      techEngineTracker.style.transform = `translate3d(0, ${currentOffset}px, 0)`;
      requestAnimationFrame(trackTechEngine);
    }

    requestAnimationFrame(trackTechEngine);

    desktopQuery.addEventListener('change', () => {
      if (!desktopQuery.matches) {
        currentOffset = 0;
        targetOffset = 0;
        techEngineTracker.style.transform = 'translate3d(0, 0, 0)';
      }
    });
  }
  // Hero section lifecycle mapping
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

  /* ── INTERACTIVE AUTOMATED BACKGROUND AUDIO CONTROLLER EXECUTION ── */
  let audioPlayer;
  let visualizerInterval;
  let audioAutoplayBootstrapped = false;

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

  // Expose standard globally expected callback for YouTube API
  window.onYouTubeIframeAPIReady = function () {
    audioPlayer = new YT.Player('ytAudioPlayerFrame', {
      height: '1',
      width: '1',
      videoId: 'pCfqB2nKi7A',
      playerVars: {
        'autoplay': 0,
        'controls': 0,
        'disablekb': 1,
        'fs': 0,
        'rel': 0,
        'modestbranding': 1
      },
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    });
  };

  // Load YouTube Player API
  const tag = document.createElement('script');
  tag.src = "https://www.youtube.com/iframe_api";
  const firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  function onPlayerReady() {
    if (audioPlayer && typeof audioPlayer.setVolume === 'function') {
      audioPlayer.setVolume(40);
    }
    document.body.addEventListener('click', bootstrapAutoplayStream, { once: true });
  }

  function bootstrapAutoplayStream() {
    if (audioAutoplayBootstrapped || !audioPlayer) return;
    if (typeof audioPlayer.playVideo === 'function') {
      audioPlayer.playVideo();
      audioAutoplayBootstrapped = true;
    }
  }

  function onPlayerStateChange(event) {
    if (event.data === YT.PlayerState.PLAYING) {
      inlineStateText.textContent = "Playing";
      playIconSvg.innerHTML = '<path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>';
      startVisualizerAnimation();
    } else {
      inlineStateText.textContent = "Paused";
      playIconSvg.innerHTML = '<path d="M8 5v14l11-7z"/>';
      stopVisualizerAnimation();
    }
  }

  function startVisualizerAnimation() {
    if (visualizerInterval) clearInterval(visualizerInterval);
    visualizerInterval = setInterval(() => {
      visualWaves.forEach(bar => {
        if (bar) {
          const bounceMetric = Math.floor(Math.random() * 12) + 3;
          bar.style.height = bounceMetric + 'px';
        }
      });
    }, 120);
  }

  function stopVisualizerAnimation() {
    clearInterval(visualizerInterval);
    visualWaves.forEach(bar => {
      if (bar) bar.style.height = '3px';
    });
  }

  function setAudioPopup(open) {
    popupContainer.classList.toggle('is-active', open);
    document.body.classList.toggle('audio-popup-open', open);
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

  popupPlayControl.addEventListener('click', () => {
    if (!audioPlayer) return;
    const currentState = audioPlayer.getPlayerState();
    if (currentState === YT.PlayerState.PLAYING) {
      audioPlayer.pauseVideo();
    } else {
      audioPlayer.playVideo();
    }
  });

  attenuationSlider.addEventListener('input', (e) => {
    if (!audioPlayer) return;
    audioPlayer.setVolume(e.target.value);
  });

  // 3. Page Loader & Smooth Page Transition Manager
  const loaderNode = document.getElementById('pageLoader');

  // Dismiss loader on page load
  const dismissLoader = () => {
    if (loaderNode) {
      setTimeout(() => {
        loaderNode.classList.add('is-hidden');
      }, 700); // Gives the logo reveal animation enough time to display beautifully
    }
  };

  // Run on load
  if (document.readyState === 'complete') {
    dismissLoader();
  } else {
    window.addEventListener('load', dismissLoader);
  }

  // Intercept click on relative local links to animate loader fade-in before navigating
  document.addEventListener('click', (e) => {
    const anchor = e.target.closest('a');
    if (!anchor) return;

    const href = anchor.getAttribute('href');
    const target = anchor.getAttribute('target');

    // Skip helper links, external links, hashes, tel/mailto, and new tab links
    if (!href ||
      href.startsWith('#') ||
      href.startsWith('mailto:') ||
      href.startsWith('tel:') ||
      target === '_blank' ||
      href.includes('://') ||
      href.startsWith('javascript:')) {
      return;
    }

    // Do not intercept hash navigation on the same page
    const currentPath = window.location.pathname;
    const cleanHref = href.split('#')[0];

    // If we're clicking a section anchor link on the same page, let it scroll naturally
    if (cleanHref === '' ||
      ((cleanHref === 'index.html' || cleanHref.endsWith('/index.html')) &&
        (currentPath.endsWith('index.html') || currentPath === '/' || currentPath.endsWith('/')))) {
      return;
    }

    // Otherwise, perform smooth transition!
    e.preventDefault();
    if (loaderNode) {
      loaderNode.classList.remove('is-hidden');
      setTimeout(() => {
        window.location.href = href;
      }, 400); // Matches transition fade-in duration
    } else {
      window.location.href = href;
    }
  });

  // Handle browser back-forward cache (BFCache) show
  window.addEventListener('pageshow', (event) => {
    if (event.persisted && loaderNode) {
      loaderNode.classList.add('is-hidden');
    }
  });
})();
