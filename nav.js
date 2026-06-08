(function() {
 var nav = document.getElementById('site-nav');
 if (nav) {
 nav.innerHTML = [
 '<div class="container">',
 '<a href="/" class="nav-logo">HOUSE<strong>,</strong> Inc.</a>',
 '<button class="nav-toggle" id="nav-toggle" aria-label="Toggle menu">☰</button>',
 '<nav class="main-nav" id="main-nav">',
 '<ul>',
 '<li><a href="/mission/">Mission</a></li>',
 '<li><a href="/programs/">Programs</a></li>',
 '<li><a href="/apply/">Apply for Help</a></li>',
 '<li><a href="/stories/">Impact</a></li>',
 '<li><a href="/transparency/">Transparency</a></li>',
 '<li><a href="/contact/">Contact</a></li>',
 '<li><a href="/donate/" class="nav-donate">Donate</a></li>',
 '</ul>',
 '</nav>',
 '</div>'
 ].join('\n');

 var toggle = document.getElementById('nav-toggle');
 var mainNav = document.getElementById('main-nav');
 if (toggle && mainNav) {
 toggle.addEventListener('click', function() {
 mainNav.classList.toggle('open');
 });
 }
 }
})();
