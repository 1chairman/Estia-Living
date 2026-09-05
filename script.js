// ── Scroll reveal ──
const reveals = document.querySelectorAll('.reveal');
if (reveals.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting) {
        setTimeout(() => e.target.classList.add('visible'), i * 80);
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  reveals.forEach(r => observer.observe(r));
}

// ── Hamburger menu toggle ──
// On mobile this opens/closes the navigation links.
// On desktop the links are always visible, so this is a placeholder
// ready for future menu items.
const hamburger = document.getElementById('hamburger');
const primaryNav = document.querySelector('nav');
if (hamburger && primaryNav) {
  hamburger.addEventListener('click', () => {
    const open = primaryNav.classList.toggle('nav-open');
    hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Close the menu when a link is tapped (mobile)
  primaryNav.querySelectorAll('.nav-link, .nav-sublink').forEach(link => {
    link.addEventListener('click', () => {
      primaryNav.classList.remove('nav-open');
      hamburger.setAttribute('aria-expanded', 'false');
    });
  });
}

// ── Formspree AJAX submit (only runs on pages with the form) ──
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', async function (e) {
    e.preventDefault();

    const name = document.getElementById('name').value.trim();
    const phone = document.getElementById('phone').value.trim();

    if (!name || !phone) {
      alert('Παρακαλώ συμπλήρωσε τουλάχιστον το όνομα και το τηλέφωνό σου.');
      return;
    }

    const btn = this.querySelector('.submit-btn');
    btn.textContent = 'Αποστολή...';
    btn.disabled = true;

    try {
      const response = await fetch(this.action, {
        method: 'POST',
        body: new FormData(this),
        headers: { 'Accept': 'application/json' }
      });

      if (response.ok) {
        this.style.display = 'none';
        document.getElementById('successMsg').style.display = 'block';
      } else {
        btn.textContent = 'Αποστολή Στοιχείων';
        btn.disabled = false;
        alert('Κάτι πήγε στραβά. Παρακαλώ δοκίμασε ξανά ή επικοινώνησε μαζί μας στο estia.cohousing@gmail.com');
      }
    } catch (err) {
      btn.textContent = 'Αποστολή Στοιχείων';
      btn.disabled = false;
      alert('Πρόβλημα σύνδεσης. Παρακαλώ δοκίμασε ξανά.');
    }
  });
}
