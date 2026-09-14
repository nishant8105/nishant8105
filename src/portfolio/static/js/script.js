/* Scroll enter + nav underline + reduced-motion respect */
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); observer.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

/* Nav underline on scroll (minimal interaction) */
const navLinks = document.querySelectorAll('.nav a');
const sections = Array.from(document.querySelectorAll('section[id]'));
function onScroll() {
  let current = '';
  sections.forEach(s => { if (window.scrollY >= s.offsetTop - 120) current = s.getAttribute('id'); });
  navLinks.forEach(a => { a.classList.toggle('active', a.getAttribute('href') === '#' + current); });
}
window.addEventListener('scroll', onScroll, { passive: true });
