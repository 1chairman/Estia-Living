// ── Mobile menu toggle ──
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  navLinks.querySelectorAll('.nav-link, .nav-sublink').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
    });
  });
}

// ── Scroll reveal ──
const reveals = document.querySelectorAll('.reveal');
if (reveals.length) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting) {
        setTimeout(() => e.target.classList.add('visible'), i * 70);
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  reveals.forEach(r => io.observe(r));
}

// ── Formspree AJAX submit (only on pages with the form) ──
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  const isEN = (document.documentElement.lang || 'el').toLowerCase().indexOf('en') === 0;
  const T = isEN ? {
    need: 'Please enter at least your name and phone number.',
    sending: 'Sending…',
    error: 'Something went wrong. Please try again or email us at estia.cohousing@gmail.com',
    conn: 'Connection problem. Please try again.'
  } : {
    need: 'Παρακαλώ συμπλήρωσε τουλάχιστον το όνομα και το τηλέφωνό σου.',
    sending: 'Αποστολή…',
    error: 'Κάτι πήγε στραβά. Δοκίμασε ξανά ή γράψε μας στο estia.cohousing@gmail.com',
    conn: 'Πρόβλημα σύνδεσης. Δοκίμασε ξανά.'
  };
  contactForm.addEventListener('submit', async function (e) {
    e.preventDefault();
    const name = (document.getElementById('name') || {}).value?.trim();
    const phone = (document.getElementById('phone') || {}).value?.trim();
    if (!name || !phone) {
      alert(T.need);
      return;
    }
    const btn = this.querySelector('.submit-btn, button[type=submit]');
    const original = btn.textContent;
    btn.textContent = T.sending;
    btn.disabled = true;
    try {
      const res = await fetch(this.action, { method: 'POST', body: new FormData(this), headers: { 'Accept': 'application/json' } });
      if (res.ok) {
        this.style.display = 'none';
        const ok = document.getElementById('successMsg');
        if (ok) ok.style.display = 'block';
      } else {
        btn.textContent = original; btn.disabled = false;
        alert(T.error);
      }
    } catch (err) {
      btn.textContent = original; btn.disabled = false;
      alert(T.conn);
    }
  });
}
