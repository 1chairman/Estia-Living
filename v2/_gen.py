# -*- coding: utf-8 -*-
# ΕΣΤΙΑ v2 — bilingual generator (EL -> v2/ , EN -> v2/en/)
import os, urllib.parse
ROOT = os.path.dirname(os.path.abspath(__file__))

# ============================================================ SVG ICONS
def svg(inner, sw="1.8", cls=""):
    c = (' class="' + cls + '"') if cls else ''
    return ('<svg' + c + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="' + sw +
            '" stroke-linecap="round" stroke-linejoin="round">' + inner + '</svg>')

CHEV  = svg('<path d="M6 9l6 6l6 -6"/>', cls="nav-chev")
FB    = svg('<path d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"/>')
LI    = svg('<path d="M4 4m0 2a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2z"/><path d="M8 11l0 5"/><path d="M8 8l0 .01"/><path d="M12 16l0 -5"/><path d="M16 16v-3a2 2 0 0 0 -4 0"/>')
BURG  = svg('<path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/>')
PHOTO = svg('<path d="M15 8h.01"/><path d="M3 6a3 3 0 0 1 3 -3h12a3 3 0 0 1 3 3v12a3 3 0 0 1 -3 3h-12a3 3 0 0 1 -3 -3v-12z"/><path d="M3 16l5 -5c.928 -.893 2.072 -.893 3 0l5 5"/><path d="M14 14l1 -1c.928 -.893 2.072 -.893 3 0l3 3"/>', sw="1.5")
CHK   = svg('<path d="M5 12l5 5l10 -10"/>')

IC_BILL   = svg('<path d="M5 21v-16a2 2 0 0 1 2 -2h10a2 2 0 0 1 2 2v16l-3 -2l-2 2l-2 -2l-2 2l-2 -2z"/><path d="M9 7h6"/><path d="M9 11h6"/><path d="M11 15h2"/>')
IC_CLEAN  = svg('<path d="M16 18a2 2 0 0 1 2 2a2 2 0 0 1 2 -2a2 2 0 0 1 -2 -2a2 2 0 0 1 -2 2z"/><path d="M16 6a2 2 0 0 1 2 2a2 2 0 0 1 2 -2a2 2 0 0 1 -2 -2a2 2 0 0 1 -2 2z"/><path d="M9 18a6 6 0 0 1 6 -6a6 6 0 0 1 -6 -6a6 6 0 0 1 -6 6a6 6 0 0 1 6 6z"/>')
IC_SOFA   = svg('<path d="M5 11a2 2 0 0 1 2 2v2h10v-2a2 2 0 1 1 4 0v4a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-4a2 2 0 0 1 2 -2z"/><path d="M5 11v-5a3 3 0 0 1 3 -3h8a3 3 0 0 1 3 3v5"/><path d="M6 19v2"/><path d="M18 19v2"/>')
IC_STETH  = svg('<path d="M6 4h-1a1 1 0 0 0 -1 1v3.5a5.5 5.5 0 0 0 11 0v-3.5a1 1 0 0 0 -1 -1h-1"/><path d="M8 15a6 6 0 1 0 12 0v-3"/><path d="M20 10m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/>')
IC_WIFI   = svg('<path d="M12 18l.01 0"/><path d="M9.172 15.172a4 4 0 0 1 5.656 0"/><path d="M6.343 12.343a8 8 0 0 1 11.314 0"/><path d="M3.515 9.515c4.686 -4.687 12.284 -4.687 17 0"/>')
IC_SHIELD = svg('<path d="M12 3a12 12 0 0 0 8.5 3a12 12 0 0 1 -8.5 15a12 12 0 0 1 -8.5 -15a12 12 0 0 0 8.5 -3"/><path d="M9 12l2 2l4 -4"/>')
IC_GLOBE  = svg('<path d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0"/><path d="M3.6 9h16.8"/><path d="M3.6 15h16.8"/><path d="M11.5 3a17 17 0 0 0 0 18"/><path d="M12.5 3a17 17 0 0 1 0 18"/>')
IC_DOC    = svg('<path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M17 21h-10a2 2 0 0 1 -2 -2v-14a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2z"/>')
IC_KEY    = svg('<path d="M16.555 3.843l3.602 3.602a2.877 2.877 0 0 1 0 4.069l-2.643 2.643a2.877 2.877 0 0 1 -4.069 0l-.301 -.301l-6.558 6.558a2 2 0 0 1 -1.239 .578l-.175 .008h-1.936a1 1 0 0 1 -.993 -.883l-.007 -.117v-1.936a2 2 0 0 1 .467 -1.284l.119 -.13l.414 -.414h2v-2h2v-2l2.144 -2.144l-.301 -.301a2.877 2.877 0 0 1 0 -4.069l2.643 -2.643a2.877 2.877 0 0 1 4.069 0z"/><path d="M15 9h.01"/>')
IC_HEART  = svg('<path d="M19.5 12.572l-7.5 7.428l-7.5 -7.428a5 5 0 1 1 7.5 -6.566a5 5 0 1 1 7.5 6.566"/>')
IC_USERS  = svg('<path d="M9 7m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0"/><path d="M3 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/><path d="M21 21v-2a4 4 0 0 0 -3 -3.85"/>')
IC_ROCKET = svg('<path d="M4 13a8 8 0 0 1 7 7a6 6 0 0 0 3 -5a9 9 0 0 0 6 -8a3 3 0 0 0 -3 -3a9 9 0 0 0 -8 6a6 6 0 0 0 -5 3"/><path d="M7 14a6 6 0 0 0 -3 6a6 6 0 0 0 6 -3"/><path d="M15 9m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"/>')
IC_SEED   = svg('<path d="M12 10a6 6 0 0 0 -6 -6h-3v2a6 6 0 0 0 6 6h3"/><path d="M12 14a6 6 0 0 1 6 -6h3v1a6 6 0 0 1 -6 6h-3"/><path d="M12 20l0 -10"/>')
IC_MAIL   = svg('<path d="M3 7a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v10a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-10z"/><path d="M3 7l9 6l9 -6"/>')
IC_PHONE  = svg('<path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2"/>')
IC_PIN    = svg('<path d="M9 11a3 3 0 1 0 6 0a3 3 0 0 0 -6 0"/><path d="M17.657 16.657l-4.243 4.243a2 2 0 0 1 -2.827 0l-4.244 -4.243a8 8 0 1 1 11.314 0z"/>')

# ============================================================ HELPERS
def ph(label, sub="", cls=""):
    inner = PHOTO + '<span>' + label + '</span>'
    if sub:
        inner += '<small>' + sub + '</small>'
    return '<div class="img-ph ' + cls + '">' + inner + '</div>'

def tick(text):
    return '<li>' + CHK + ' ' + text + '</li>'

def card(icon, title, body):
    return ('        <div class="card reveal"><div class="card-icon">' + icon + '</div><h3>' + title + '</h3><p>' + body + '</p></div>\n')

def mailto(role, lang):
    subj = urllib.parse.quote(('Αίτηση: ' if lang == 'el' else 'Application: ') + role)
    return 'mailto:estia.cohousing@gmail.com?subject=' + subj

# ============================================================ UI STRINGS
UI = {
 'el': {
  'brand': 'ΕΣΤΙΑ', 'brand_sub': 'ΖΟΥΜΕ ΜΑΖΙ',
  'home':'Αρχική','cohousing':'Συστέγαση','model':'Το μοντέλο μας',
  'technology':'Τεχνολογία','history':'Ιστορία του Cohousing','research':'Έρευνες & Τεκμηρίωση',
  'membership':'Γίνε Μέλος','municipalities':'Για Δήμους','expats':'Για Ξένους',
  'about':'Ποιοι Είμαστε','aboutus':'Ποιοι Είμαστε','careers':'Καριέρα',
  'updates':'Ενημέρωση','news':'Νέα','blog':'Blog','contact':'Επικοινωνία',
  'menu':'Μενού',
  'f_tag':'Συνεργατική διαβίωση για ανθρώπους 60+ στην Αθήνα. Αυτονομία, κοινότητα και ποιότητα ζωής.',
  'f_explore':'Εξερεύνηση','f_company':'Η ΕΣΤΙΑ','f_contact':'Επικοινωνία',
  'f_form':'Φόρμα επικοινωνίας','f_bottom':'© 2026 ΕΣΤΙΑ · Αθήνα · Συνεργατική Διαβίωση 60+',
 },
 'en': {
  'brand': 'ESTIA', 'brand_sub': 'LIVING TOGETHER',
  'home':'Home','cohousing':'Co-Housing','model':'Our Model',
  'technology':'Technology','history':'History of Cohousing','research':'Research & Evidence',
  'membership':'Membership','municipalities':'For Municipalities','expats':'For Expats',
  'about':'About','aboutus':'About Us','careers':'Careers',
  'updates':'Updates','news':'News','blog':'Blog','contact':'Contact',
  'menu':'Menu',
  'f_tag':'Co-living for people 60+ in Athens. Autonomy, community and quality of life.',
  'f_explore':'Explore','f_company':'Company','f_contact':'Contact',
  'f_form':'Contact form','f_bottom':'© 2026 ESTIA · Athens · Senior Co-Living 60+',
 },
}

# ============================================================ HEAD
def head(lang, p, title, desc):
    return ('<!DOCTYPE html>\n<html lang="' + lang + '">\n\n<head>\n'
    '  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    '  <title>' + title + '</title>\n'
    '  <meta name="description" content="' + desc + '">\n'
    '  <link rel="icon" href="' + p + 'logo.svg" type="image/svg+xml">\n'
    '  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">\n'
    '  <link rel="stylesheet" href="' + p + 'styles.css">\n</head>\n\n<body>\n')

# ============================================================ NAV
def nav(lang, p, active, sub):
    U = UI[lang]
    def a(key, href, label):
        cls = "nav-link active" if active == key else "nav-link"
        return '<a href="' + href + '" class="' + cls + '">' + label + '</a>'
    def s(key, href, label):
        cls = "nav-sublink active" if sub == key else "nav-sublink"
        return '<a href="' + href + '" class="' + cls + '">' + label + '</a>'
    co_cls = "nav-link active" if active == "cohousing" else "nav-link"
    ab_cls = "nav-link active" if active == "about" else "nav-link"
    up_cls = "nav-link active" if active == "updates" else "nav-link"
    # language switch targets
    if lang == 'el':
        el_href, en_href = '#', 'en/' + CURRENT[0]
        el_a, en_a = 'active', ''
    else:
        el_href, en_href = '../' + CURRENT[0], '#'
        el_a, en_a = '', 'active'
    lang_switch = ('        <div class="lang-switch">\n'
        '          <a href="' + el_href + '" class="' + el_a + '" aria-label="Ελληνικά">ΕΛ</a>\n'
        '          <span>/</span>\n'
        '          <a href="' + en_href + '" class="' + en_a + '" aria-label="English">EN</a>\n'
        '        </div>\n')
    return (
    '  <header class="site-header">\n    <nav class="nav">\n'
    '      <a href="index.html" class="brand">\n'
    '        <img src="' + p + 'logo.svg" alt="' + U['brand'] + '">\n'
    '        <span class="brand-txt">' + U['brand'] + '<span>' + U['brand_sub'] + '</span></span>\n'
    '      </a>\n\n'
    '      <div class="nav-links" id="navLinks">\n'
    '        ' + a("home", "index.html", U['home']) + '\n'
    '        <div class="nav-dd">\n'
    '          <a href="cohousing.html" class="' + co_cls + '">' + U['cohousing'] + ' ' + CHEV + '</a>\n'
    '          <div class="nav-submenu">\n'
    '            ' + s("model", "cohousing.html", U['model']) + '\n'
    '            ' + s("technology", "technology.html", U['technology']) + '\n'
    '            ' + s("history", "history.html", U['history']) + '\n'
    '            ' + s("research", "research.html", U['research']) + '\n'
    '          </div>\n'
    '        </div>\n'
    '        ' + a("membership", "membership.html", U['membership']) + '\n'
    '        ' + a("municipalities", "municipalities.html", U['municipalities']) + '\n'
    '        ' + a("expats", "expats.html", U['expats']) + '\n'
    '        <div class="nav-dd">\n'
    '          <a href="about.html" class="' + ab_cls + '">' + U['about'] + ' ' + CHEV + '</a>\n'
    '          <div class="nav-submenu">\n'
    '            ' + s("aboutus", "about.html", U['aboutus']) + '\n'
    '            ' + s("careers", "careers.html", U['careers']) + '\n'
    '          </div>\n'
    '        </div>\n'
    '        <div class="nav-dd">\n'
    '          <a href="news.html" class="' + up_cls + '">' + U['updates'] + ' ' + CHEV + '</a>\n'
    '          <div class="nav-submenu">\n'
    '            ' + s("news", "news.html", U['news']) + '\n'
    '            ' + s("blog", "blog.html", U['blog']) + '\n'
    '          </div>\n'
    '        </div>\n'
    '        <a href="contact.html" class="nav-link nav-contact-m">' + U['contact'] + '</a>\n'
    '      </div>\n\n'
    '      <div class="nav-side">\n'
    '        <div class="socials">\n'
    '          <a href="https://www.facebook.com/profile.php?id=61590165540577" target="_blank" rel="noopener noreferrer" class="social fb" aria-label="Facebook">' + FB + '</a>\n'
    '          <a href="#" class="social li" aria-label="LinkedIn">' + LI + '</a>\n'
    '        </div>\n'
    + lang_switch +
    '        <span class="nav-divider"></span>\n'
    '        <a href="contact.html" class="btn btn-primary nav-cta" style="padding:0.62rem 1.3rem;">' + U['contact'] + '</a>\n'
    '        <button class="hamburger" id="hamburger" aria-label="' + U['menu'] + '" aria-expanded="false">' + BURG + '</button>\n'
    '      </div>\n'
    '    </nav>\n  </header>\n\n')

# ============================================================ FOOTER
def footer(lang, p):
    U = UI[lang]
    links = {
      'model':U['model'],'technology':U['technology'],'membership':U['membership'],
      'municipalities':U['municipalities'],'expats':U['expats'],'about':U['aboutus'],
      'careers':U['careers'],'news':U['news'],'blog':U['blog'],'research':U['research'],
    }
    return (
    '  <footer class="site-footer">\n    <div class="wrap">\n      <div class="footer-grid">\n'
    '        <div class="footer-brand">\n'
    '          <div class="brand" style="margin-bottom:0;">\n'
    '            <img src="' + p + 'logo.svg" alt="' + U['brand'] + '" style="height:34px;">\n'
    '            <span class="brand-txt">' + U['brand'] + '<span>' + U['brand_sub'] + '</span></span>\n'
    '          </div>\n'
    '          <p>' + U['f_tag'] + '</p>\n'
    '        </div>\n'
    '        <div class="footer-col">\n          <h4>' + U['f_explore'] + '</h4>\n'
    '          <a href="cohousing.html">' + links['model'] + '</a>\n'
    '          <a href="technology.html">' + links['technology'] + '</a>\n'
    '          <a href="membership.html">' + links['membership'] + '</a>\n'
    '          <a href="municipalities.html">' + links['municipalities'] + '</a>\n'
    '          <a href="expats.html">' + links['expats'] + '</a>\n'
    '        </div>\n'
    '        <div class="footer-col">\n          <h4>' + U['f_company'] + '</h4>\n'
    '          <a href="about.html">' + links['about'] + '</a>\n'
    '          <a href="careers.html">' + links['careers'] + '</a>\n'
    '          <a href="news.html">' + links['news'] + '</a>\n'
    '          <a href="blog.html">' + links['blog'] + '</a>\n'
    '          <a href="research.html">' + links['research'] + '</a>\n'
    '        </div>\n'
    '        <div class="footer-col">\n          <h4>' + U['f_contact'] + '</h4>\n'
    '          <a href="mailto:estia.cohousing@gmail.com">estia.cohousing@gmail.com</a>\n'
    '          <a href="contact.html">' + U['f_form'] + '</a>\n'
    '          <div class="socials" style="margin-top:0.8rem;">\n'
    '            <a href="https://www.facebook.com/profile.php?id=61590165540577" target="_blank" rel="noopener noreferrer" class="social fb" aria-label="Facebook">' + FB + '</a>\n'
    '            <a href="#" class="social li" aria-label="LinkedIn">' + LI + '</a>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="footer-bottom">\n'
    '        <p>' + U['f_bottom'] + '</p>\n'
    '        <p>estia.live</p>\n'
    '      </div>\n    </div>\n  </footer>\n\n'
    '  <script src="' + p + 'script.js"></script>\n</body>\n\n</html>\n')

# ============================================================ SHARED BLOCKS
def hero(eyebrow, title_html, sub, ctas, vlabel, vsub="", vcls=""):
    return ('  <section class="hero">\n    <div class="wrap">\n      <div class="hero-grid">\n'
    '        <div class="reveal">\n'
    '          <p class="eyebrow">' + eyebrow + '</p>\n'
    '          <h1 class="hero-title">' + title_html + '</h1>\n'
    '          <p class="hero-sub">' + sub + '</p>\n'
    '          <div class="hero-cta">' + ctas + '</div>\n'
    '        </div>\n'
    '        <div class="hero-visual reveal">' + ph(vlabel, vsub, vcls) + '</div>\n'
    '      </div>\n    </div>\n  </section>\n\n')

def cta_band(title, text, ctas):
    return ('  <section class="section cta-band">\n    <div class="wrap">\n'
    '      <h2 class="h-lg reveal">' + title + '</h2>\n'
    '      <p class="reveal">' + text + '</p>\n'
    '      <div class="hero-cta reveal">' + ctas + '</div>\n'
    '    </div>\n  </section>\n\n')

def sechead(eyebrow, h_html, lead="", center=False, size="h-lg"):
    c = " center" if center else ""
    lead_html = ('<p class="lead" style="margin-top:1rem;">' + lead + '</p>') if lead else ""
    return ('      <div class="sec-head' + c + ' reveal"><p class="eyebrow">' + eyebrow +
            '</p><h2 class="' + size + '">' + h_html + '</h2>' + lead_html + '</div>\n')

# ============================================================ PAGE BODIES
CURRENT = ['index.html']  # set per page so nav lang-switch points to the twin

def body_home(lang):
    EL = lang == 'el'
    if EL:
        H = hero('Συνεργατική Διαβίωση · Αθήνα',
            'Μετά τα 60,<br><em>η ζωή ανθίζει.</em>',
            'Αυτόνομη συστέγαση για ανθρώπους άνω των 60 — ο δικός σου ιδιωτικός χώρος, μέσα σε μια μικρή, δεμένη κοινότητα ανθρώπων που ταιριάζουν μεταξύ τους.',
            '<a href="membership.html" class="btn btn-primary">Γίνε Μέλος</a> <a href="cohousing.html" class="btn btn-ghost">Δες το μοντέλο</a>',
            'Φωτογραφία hero', 'πραγματική φωτο κοινότητας / χώρου')
        stats = [('20','Κάτοικοι ανά κοινότητα'),('21<span style="font-size:0.5em"> τ.μ.</span>','Ιδιωτικός χώρος ανά άτομο'),
                 ('50+','Χρόνια cohousing διεθνώς'),('100%','All-inclusive μηνιαία συνδρομή')]
        mission_eye, mission_h = 'Η Αποστολή μας', 'Η μοναξιά δεν είναι <em>αναπόφευκτη.</em>'
        mission_p = ('<p>Η έλλειψη ποιοτικών σπιτιών σε ωραία τοποθεσία, η δύσκολη πρόσβαση σε υπηρεσίες υγείας και η μοναξιά της πόλης μάς έδωσαν το κίνητρο να δράσουμε.</p>'
                     '<p>Αποστολή μας είναι να μετατρέψουμε τις δεκαετίες μετά τα 60 στην πιο ποιοτική περίοδο της ζωής — με <strong>αυτονομία, ασφάλεια</strong> και χωρίς το άγχος της απομόνωσης.</p>')
        serv_eye, serv_h = 'Τι περιλαμβάνεται', 'Όλα όσα χρειάζεσαι, <em>στον ίδιο χώρο.</em>'
        services = [
          (IC_BILL,'Κοινόχρηστα & Λογαριασμοί','Πλήρης κάλυψη ρεύματος, θέρμανσης, νερού και τηλεφωνίας. Καμία έκπληξη, καμία αγωνία.'),
          (IC_CLEAN,'Καθαριότητα','Επαγγελματικός καθαρισμός του διαμερίσματος κάθε εβδομάδα — το σπίτι πάντα φρέσκο.'),
          (IC_SOFA,'Κοινόχρηστοι Χώροι','Σαλόνι, βιβλιοθήκη, κήπος και χώρος για μπάρμπεκιου — εκεί όπου γεννιούνται οι φιλίες.'),
          (IC_STETH,'Μηνιαία Επίσκεψη Γιατρού','Ο γιατρός έρχεται στο σπίτι. Τακτικός έλεγχος, συνταγογράφηση και προληπτική φροντίδα.'),
          (IC_WIFI,'Υψηλές Ταχύτητες Σύνδεσης','Οπτική ίνα σε όλους τους χώρους — για να μένεις κοντά σε όσους αγαπάς.'),
          (IC_SHIELD,'24/7 Υποστήριξη Ασφάλειας','Σύστημα έκτακτης ανάγκης με προσωπικό κουμπί SOS — γιατί η ασφάλεια δεν διαπραγματεύεται.'),
        ]
        vis_eye, vis_h = 'Το Όραμά μας', 'Να μεγαλώνεις σημαίνει <em>να συνδέεσαι βαθύτερα.</em>'
        pillars = [('Σύνδεση','Σχεδιάζουμε χώρους όπου οι τυχαίες συναντήσεις γίνονται φιλίες, και οι φιλίες οικογένεια.'),
                   ('Αξιοπρέπεια','Κάθε κάτοικος είναι μέλος της κοινότητας — όχι ενοικιαστής, όχι ασθενής. Εδώ έχεις λόγο.'),
                   ('Ταίριασμα','Οι άνθρωποι σε κάθε σπίτι ταιριάζουν μεταξύ τους. Αυτό είναι που κάνει μια κοινότητα να δουλεύει.')]
        cta = ('Θέλεις να μάθεις περισσότερα;','Άφησε τα στοιχεία σου και θα επικοινωνήσουμε μαζί σου για να σου εξηγήσουμε αναλυτικά το μοντέλο, το κόστος και τις διαθέσιμες θέσεις.',
               '<a href="contact.html" class="btn btn-primary">Επικοινώνησε μαζί μας</a> <a href="membership.html" class="btn btn-ghost">Δες πώς γίνεσαι μέλος</a>')
        mvis = ('Φωτογραφία','στιγμή κοινότητας / παρέα')
    else:
        H = hero('Co-Living · Athens',
            'After 60,<br><em>life blossoms.</em>',
            'Independent co-living for people over 60 — your own private space, inside a small, close-knit community of people who truly fit together.',
            '<a href="membership.html" class="btn btn-primary">Become a Member</a> <a href="cohousing.html" class="btn btn-ghost">See the model</a>',
            'Hero photo', 'real photo of the community / space')
        stats = [('20','Residents per community'),('21<span style="font-size:0.5em"> m²</span>','Private space per person'),
                 ('50+','Years of cohousing worldwide'),('100%','All-inclusive monthly fee')]
        mission_eye, mission_h = 'Our Mission', 'Loneliness is not <em>inevitable.</em>'
        mission_p = ('<p>The shortage of quality homes in beautiful locations, the difficulty of accessing healthcare, and the loneliness of city life gave us the drive to act.</p>'
                     '<p>Our mission is to turn the decades after 60 into the most fulfilling period of life — with <strong>autonomy, safety</strong> and without the anxiety of isolation.</p>')
        serv_eye, serv_h = "What's included", 'Everything you need, <em>in one place.</em>'
        services = [
          (IC_BILL,'Utilities & Bills','Full coverage of electricity, heating, water and telephony. No surprises, no worries.'),
          (IC_CLEAN,'Cleaning','Professional cleaning of your apartment every week — a home that always feels fresh.'),
          (IC_SOFA,'Shared Spaces','Lounge, library, garden and a barbecue area — where friendships are born.'),
          (IC_STETH,'Monthly Doctor Visit','The doctor comes to you. Regular check-ups, prescriptions and preventive care.'),
          (IC_WIFI,'High-Speed Connectivity','Fibre throughout — so you stay close to the people you love.'),
          (IC_SHIELD,'24/7 Safety Support','An emergency system with a personal SOS button — because safety is non-negotiable.'),
        ]
        vis_eye, vis_h = 'Our Vision', 'Growing older means <em>connecting more deeply.</em>'
        pillars = [('Connection','We design spaces where chance encounters become friendships, and friendships become family.'),
                   ('Dignity','Every resident is a member of the community — not a tenant, not a patient. Here, you have a voice.'),
                   ('Matching','The people in each home genuinely fit together. That is what makes a community work.')]
        cta = ('Want to learn more?','Leave your details and we will get in touch to walk you through the model, the cost and the available places.',
               '<a href="contact.html" class="btn btn-primary">Get in touch</a> <a href="membership.html" class="btn btn-ghost">See how to join</a>')
        mvis = ('Photo','a moment of community / company')

    stats_html = ""
    for num, lab in stats:
        stats_html += '        <div class="stat reveal"><div class="stat-num">' + num + '</div><div class="stat-label">' + lab + '</div></div>\n'
    serv_html = ""
    for ic, t, d in services:
        serv_html += card(ic, t, d)
    pil_html = ""
    for t, d in pillars:
        pil_html += '        <div class="pillar reveal"><h3>' + t + '</h3><p>' + d + '</p></div>\n'

    return (H +
     '  <section class="section tight cream">\n    <div class="wrap">\n      <div class="stats">\n' + stats_html + '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section">\n    <div class="wrap">\n      <div class="split">\n'
     '        <div class="split-text reveal">\n          <p class="eyebrow">' + mission_eye + '</p>\n'
     '          <h2 class="h-lg">' + mission_h + '</h2>\n'
     '          <div class="prose" style="margin-top:1.5rem;">' + mission_p + '</div>\n        </div>\n'
     '        <div class="split-visual reveal">' + ph(mvis[0], mvis[1]) + '</div>\n'
     '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section warm">\n    <div class="wrap">\n' + sechead(serv_eye, serv_h) +
     '      <div class="cards">\n' + serv_html + '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section">\n    <div class="wrap">\n' + sechead(vis_eye, vis_h) +
     '      <div class="pillars">\n' + pil_html + '      </div>\n    </div>\n  </section>\n\n' +
     cta_band(*cta))

def body_cohousing(lang):
    EL = lang == 'el'
    if EL:
        H = hero('Συστέγαση / Co-Housing','Το μοντέλο<br><em>μας.</em>',
            'Ο δικός σου ιδιωτικός χώρος, με όλη την άνεση και την ιδιωτικότητα ενός σπιτιού — και, δίπλα, μια ζεστή κοινότητα και κοινόχρηστοι χώροι για να μοιράζεσαι τη μέρα σου.',
            '<a href="membership.html" class="btn btn-primary">Γίνε Μέλος</a> <a href="contact.html" class="btn btn-ghost">Ρώτησέ μας</a>',
            'Ενδεικτική απεικόνιση χώρου','render (AI) — προς αντικατάσταση')
        priv = ('Ο ιδιωτικός σου χώρος','Δικό σου σπίτι, <em>όχι δωμάτιο.</em>',
            '<p>Κάθε κάτοικος έχει <strong>21 τ.μ. αποκλειστικά δικά του</strong>: υπνοδωμάτιο με κρεβάτι, δικό του μπάνιο, γραφείο και ντουλάπες. Μοιράζεσαι ένα άνετο σαλονάκι με καναπέ και κουζίνα με ακόμη ένα άτομο — κάποιον που ταιριάζει μαζί σου ή έναν δικό σου φίλο.</p>',
            [ '21 τ.μ. ιδιωτικός χώρος ανά άτομο','Δικό σου μπάνιο, γραφείο και ντουλάπες',
              'Κοινό σαλονάκι & κουζίνα με ένα ακόμη άτομο ή φίλο σου',
              'Για ζευγάρια: <strong>27 τ.μ.</strong> με διπλό κρεβάτι — ολόκληρο το διαμέρισμα (~50 τ.μ.) δικό τους'],
            'Ενδεικτική απεικόνιση','ιδιωτικός χώρος / υπνοδωμάτιο')
        shared = ('Κοινόχρηστοι χώροι','Η καρδιά της <em>κοινότητας.</em>',
            '<p>Στον κάτω όροφο βρίσκεται η καρδιά του σπιτιού: χώροι για να συναντιέσαι, να χαλαρώνεις και να περνάς όμορφα, όποτε το θελήσεις.</p>',
            ['Σαλόνι & βιβλιοθήκη','Εξωτερικός χώρος για μπάρμπεκιου & μαζώξεις','Κήπος','Ιδιωτικός χώρος στάθμευσης','Αίθουσα άθλησης / εκγύμνασης'],
            'Ενδεικτική απεικόνιση','κοινόχρηστο σαλόνι / κήπος')
        gal_eye, gal_h = 'Απεικονίσεις χώρων', 'Έτσι τους <em>οραματιζόμαστε.</em>'
        gal_lead = 'Οι παρακάτω εικόνες είναι ενδεικτικές απεικονίσεις των χώρων που σχεδιάζουμε — για να πάρεις μια ιδέα. Με τον καιρό θα προσθέσουμε πραγματικές φωτογραφίες.'
        gal_lbl = 'Render'
        cta = ('Σε ενδιαφέρει μια θέση;','Μάθε πώς γίνεσαι μέλος της κοινότητας — από την πρώτη γνωριμία μέχρι τη μετακόμιση.',
               '<a href="membership.html" class="btn btn-primary">Δες πώς γίνεσαι μέλος</a> <a href="history.html" class="btn btn-ghost">Ιστορία του Cohousing</a>')
    else:
        H = hero('Co-Housing','Our<br><em>model.</em>',
            'Your own private space, with all the comfort and privacy of a home — and, right beside it, a warm community and shared areas to share your day.',
            '<a href="membership.html" class="btn btn-primary">Become a Member</a> <a href="contact.html" class="btn btn-ghost">Ask us</a>',
            'Indicative render of a space','render (AI) — to be replaced')
        priv = ('Your private space','A home of your own, <em>not a room.</em>',
            '<p>Each resident has <strong>21 m² entirely their own</strong>: a bedroom, their own bathroom, a study and wardrobes. You share a comfortable lounge with a sofa and a kitchen with one other person — someone who fits with you, or a friend of yours.</p>',
            [ '21 m² of private space per person','Your own bathroom, study and wardrobes',
              'A shared lounge & kitchen with one other person or a friend',
              'For couples: <strong>27 m²</strong> with a double bed — the whole apartment (~50 m²) is theirs'],
            'Indicative render','private space / bedroom')
        shared = ('Shared spaces','The heart of the <em>community.</em>',
            '<p>Downstairs is the heart of the home: spaces to meet, relax and enjoy yourself, whenever you feel like it.</p>',
            ['Lounge & library','Outdoor area for barbecues & gatherings','Garden','Private parking','Gym / exercise room'],
            'Indicative render','shared lounge / garden')
        gal_eye, gal_h = 'Renders of the spaces', 'This is how we <em>envision them.</em>'
        gal_lead = 'The images below are indicative renders of the spaces we are designing — to give you an idea. Over time we will add real photos.'
        gal_lbl = 'Render'
        cta = ('Interested in a place?','Find out how to join the community — from the first conversation to moving in.',
               '<a href="membership.html" class="btn btn-primary">See how to join</a> <a href="history.html" class="btn btn-ghost">History of Cohousing</a>')

    def block(data, warm=False, reverse=False):
        eye, h, prose, ticks, vl, vs = data
        ticks_html = "".join('            ' + tick(x) + '\n' for x in ticks)
        sec = 'section warm' if warm else 'section'
        rev = ' reverse' if reverse else ''
        return ('  <section class="' + sec + '">\n    <div class="wrap">\n      <div class="split' + rev + '">\n'
            '        <div class="split-text reveal">\n          <p class="eyebrow">' + eye + '</p>\n'
            '          <h2 class="h-lg">' + h + '</h2>\n'
            '          <div class="prose" style="margin-top:1.3rem;">' + prose + '</div>\n'
            '          <ul class="ticks">\n' + ticks_html + '          </ul>\n        </div>\n'
            '        <div class="split-visual reveal">' + ph(vl, vs, "tall") + '</div>\n'
            '      </div>\n    </div>\n  </section>\n\n')

    gallery = '      <div class="gallery">\n'
    for i in range(1, 7):
        gallery += '        <div class="img-ph reveal">' + PHOTO + '<span>' + gal_lbl + ' ' + str(i) + '</span></div>\n'
    gallery += '      </div>\n'

    return (H + block(priv) + block(shared, warm=True, reverse=True) +
     '  <section class="section">\n    <div class="wrap">\n' + sechead(gal_eye, gal_h, gal_lead) + gallery +
     '    </div>\n  </section>\n\n' + cta_band(*cta))

def body_technology(lang):
    EL = lang == 'el'
    if EL:
        H = hero('Συστέγαση / Co-Housing','Η τεχνολογία<br><em>πίσω από την κοινότητα.</em>',
            "Μια κοινότητα δουλεύει όταν οι άνθρωποι ταιριάζουν. Γι' αυτό στην ΕΣΤΙΑ η τεχνολογία δεν είναι αυτοσκοπός — είναι το εργαλείο που φέρνει τους σωστούς ανθρώπους κοντά.",
            '<a href="contact.html" class="btn btn-primary">Επικοινωνία</a> <a href="cohousing.html" class="btn btn-ghost">Το μοντέλο μας</a>',
            'Απεικόνιση','έξυπνο σπίτι / πλατφόρμα')
        eye, h = 'Τι χρησιμοποιούμε', 'Πέντε πυλώνες <em>τεχνολογίας.</em>'
        items = [
         ('Έξυπνο Σπίτι','Αυτοματισμοί φωτισμού, θέρμανσης και ασφάλειας που κάνουν την καθημερινότητα απλή, άνετη και ασφαλή.'),
         ('Βιωσιμότητα','Ενεργειακή αναβάθμιση, ηλιακή ενέργεια και αντλίες θερμότητας — χαμηλότερο κόστος και μικρότερο αποτύπωμα.'),
         ('Ταίριασμα Ανθρώπων','Ειδικό λογισμικό (υπό ανάπτυξη) που βοηθά να συνυπάρχουν άνθρωποι που ταιριάζουν — η καρδιά του μοντέλου μας.'),
         ('Αναφορά & Ενημέρωση','Πλατφόρμα κεντρικής ενημέρωσης και αναφοράς παραπόνων — που μπορεί να αξιοποιηθεί και από άλλους παρόχους, συνδρομητές και πολυκατοικίες.'),
         ('Αλγόριθμος Περιοχής','Επιλογή της καταλληλότερης περιοχής με βάση τις ανάγκες των ανθρώπων που έχουν εκδηλώσει ενδιαφέρον.'),
        ]
        note = '<p><strong>Σημείωση:</strong> μέρος του λογισμικού βρίσκεται υπό ανάπτυξη. [ΣΥΜΠΛΗΡΩΝΕΤΑΙ: πόσες λεπτομέρειες θέλουμε να αποκαλύψουμε δημόσια.]</p>'
        cta = ('Θες να μάθεις περισσότερα;','Επικοινώνησε μαζί μας και θα σου εξηγήσουμε πώς η τεχνολογία κάνει τη διαφορά.',
               '<a href="contact.html" class="btn btn-primary">Επικοινωνία</a> <a href="cohousing.html" class="btn btn-ghost">Το μοντέλο μας</a>')
    else:
        H = hero('Co-Housing','The technology<br><em>behind the community.</em>',
            'A community works when the people fit together. That is why, at ESTIA, technology is never the goal in itself — it is the tool that brings the right people together.',
            '<a href="contact.html" class="btn btn-primary">Contact</a> <a href="cohousing.html" class="btn btn-ghost">Our model</a>',
            'Illustration','smart home / platform')
        eye, h = 'What we use', 'Five pillars <em>of technology.</em>'
        items = [
         ('Smart Home','Lighting, heating and safety automation that makes everyday life simple, comfortable and secure.'),
         ('Sustainability','Energy upgrades, solar power and heat pumps — lower costs and a smaller footprint.'),
         ('People Matching','Dedicated software (in development) that helps compatible people live well together — the heart of our model.'),
         ('Reporting & Info','A central information and complaint-reporting platform — one that other providers, subscribers and apartment buildings could use too.'),
         ('Location Algorithm','Choosing the most suitable area based on the needs of the people who have expressed interest.'),
        ]
        note = '<p><strong>Note:</strong> part of the software is in development. [TO BE COMPLETED: how much detail we want to reveal publicly.]</p>'
        cta = ('Want to know more?','Get in touch and we will explain how technology makes the difference.',
               '<a href="contact.html" class="btn btn-primary">Contact</a> <a href="cohousing.html" class="btn btn-ghost">Our model</a>')
    cards = "".join(card(CHK, t, d) for t, d in items)
    return (H + '  <section class="section warm">\n    <div class="wrap">\n' + sechead(eye, h) +
     '      <div class="cards">\n' + cards + '      </div>\n'
     '      <div class="callout reveal" style="margin-top:3rem;">' + note + '</div>\n'
     '    </div>\n  </section>\n\n' + cta_band(*cta))

def body_membership(lang):
    EL = lang == 'el'
    if EL:
        H = hero('Συμμετοχή','Γίνε<br><em>Μέλος.</em>',
            'Από την πρώτη γνωριμία μέχρι τη μετακόμιση — ένα απλό, ανθρώπινο ταξίδι, χωρίς πιέσεις.',
            '<a href="contact.html" class="btn btn-primary">Επικοινωνία</a> <a href="cohousing.html" class="btn btn-ghost">Δες το μοντέλο</a>',
            'Φωτογραφία','στιγμή καλωσορίσματος')
        eye, h = 'Τα βήματα', 'Πώς γίνεσαι <em>μέλος.</em>'
        steps = [
         ('Αρχική Επικοινωνία','Μας αφήνεις τα στοιχεία σου μέσω της φόρμας — χωρίς καμία δέσμευση.'),
         ('Τηλεφωνική Γνωριμία','Σε παίρνουμε τηλέφωνο, σου εξηγούμε το μοντέλο και ακούμε τις δικές σου ερωτήσεις.'),
         ('Συνάντηση από Κοντά','Γνωριζόμαστε καλύτερα — τα ενδιαφέροντα, οι ανάγκες και ο τρόπος ζωής που αναζητάς.'),
         ('[ΣΥΜΠΛΗΡΩΝΕΤΑΙ] Επιλογή & Ταίριασμα','[Περιγραφή του ενδιάμεσου βήματος: επιλογή διαμερίσματος και ταίριασμα συγκατοίκου.]'),
         ('[ΣΥΜΠΛΗΡΩΝΕΤΑΙ] Συμφωνία','[Περιγραφή: συμφωνητικό, όροι συμμετοχής, κόστος.]'),
         ('Μετακόμιση','Καλωσορίζεσαι στο νέο σου σπίτι και στην κοινότητά σου.'),
        ]
        prop = ('Αξιοποίηση Περιουσίας','Το παλιό σου σπίτι <em>δουλεύει για εσένα.</em>',
            '<p>Δεν χρειάζεται να πουλήσεις. Αν το επιθυμείς, αναλαμβάνουμε την <strong>ανακαίνιση και την ενοικίαση</strong> του προηγούμενου σπιτιού σου, ώστε να σου αποφέρει ένα σημαντικό μηνιαίο εισόδημα.</p>',
            '[ΣΥΜΠΛΗΡΩΝΕΤΑΙ: οι ακριβείς όροι της αξιοποίησης — ποιος αναλαμβάνει τι, ποσοστά, διάρκεια.]',
            'Φωτογραφία','ανακαινισμένο διαμέρισμα')
        cta = ('Έτοιμος να ξεκινήσεις;','Άφησε τα στοιχεία σου και κάνουμε το πρώτο βήμα μαζί.',
               '<a href="contact.html" class="btn btn-primary">Επικοινωνία</a> <a href="cohousing.html" class="btn btn-ghost">Δες το μοντέλο</a>')
    else:
        H = hero('Joining','Become<br><em>a Member.</em>',
            'From the first conversation to moving in — a simple, human journey, with no pressure.',
            '<a href="contact.html" class="btn btn-primary">Contact</a> <a href="cohousing.html" class="btn btn-ghost">See the model</a>',
            'Photo','a moment of welcome')
        eye, h = 'The steps', 'How you <em>become a member.</em>'
        steps = [
         ('Initial Contact','You leave your details through the form — with no commitment at all.'),
         ('A Phone Introduction','We call you, explain the model, and listen to your own questions.'),
         ('Meeting in Person','We get to know each other better — your interests, your needs and the lifestyle you are looking for.'),
         ('[TO BE COMPLETED] Selection & Matching','[Description of the intermediate step: choosing an apartment and matching a housemate.]'),
         ('[TO BE COMPLETED] Agreement','[Description: the agreement, terms of participation, cost.]'),
         ('Moving In','You are welcomed into your new home and your community.'),
        ]
        prop = ('Making Your Property Work','Your old home <em>working for you.</em>',
            '<p>You do not need to sell. If you wish, we take on the <strong>renovation and the renting</strong> of your previous home, so that it earns you a meaningful monthly income.</p>',
            '[TO BE COMPLETED: the exact terms — who handles what, percentages, duration.]',
            'Photo','a renovated apartment')
        cta = ('Ready to begin?','Leave your details and we take the first step together.',
               '<a href="contact.html" class="btn btn-primary">Contact</a> <a href="cohousing.html" class="btn btn-ghost">See the model</a>')
    steps_html = ""
    for i, (t, d) in enumerate(steps, 1):
        steps_html += '        <div class="step reveal"><div class="step-num">' + str(i) + '</div><div><h3>' + t + '</h3><p>' + d + '</p></div></div>\n'
    pe, ph_h, pp, pc, pvl, pvs = prop
    return (H +
     '  <section class="section">\n    <div class="wrap">\n' + sechead(eye, h) +
     '      <div class="steps">\n' + steps_html + '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section warm">\n    <div class="wrap">\n      <div class="split">\n'
     '        <div class="split-text reveal">\n          <p class="eyebrow">' + pe + '</p>\n'
     '          <h2 class="h-lg">' + ph_h + '</h2>\n'
     '          <div class="prose" style="margin-top:1.3rem;">' + pp + '</div>\n'
     '          <div class="callout reveal"><p>' + pc + '</p></div>\n        </div>\n'
     '        <div class="split-visual reveal">' + ph(pvl, pvs, "tall") + '</div>\n'
     '      </div>\n    </div>\n  </section>\n\n' + cta_band(*cta))

def body_municipalities(lang):
    EL = lang == 'el'
    if EL:
        H = hero('Για Δήμους','Μια λύση για τους<br><em>ηλικιωμένους σας.</em>',
            'Ο δήμος διαθέτει ένα ακίνητο. Εμείς το ανακαινίζουμε και το διαμορφώνουμε. Σε αντάλλαγμα, ο δήμος εξασφαλίζει θέσεις για δικούς του κατοίκους.',
            '<a href="contact.html" class="btn btn-primary">Επικοινωνήστε μαζί μας</a>',
            'Απεικόνιση','δημοτικό κτίριο / ανακαίνιση')
        split = ('Η συνεργασία','Μια συμφωνία <em>που ωφελεί όλους.</em>',
            '<p>Πολλοί δήμοι έχουν ακίνητα που μένουν αναξιοποίητα — και, ταυτόχρονα, ηλικιωμένους που ζουν σε κακές συνθήκες. Η ΕΣΤΙΑ συνδέει τα δύο.</p>',
            ['Ο δήμος διαθέτει το ακίνητο — χωρίς κεφαλαιακή δαπάνη.','Εμείς αναλαμβάνουμε την ανακαίνιση και τη λειτουργία.',
             'Ο δήμος παίρνει ποσοστό των θέσεων [ΣΥΜΠΛΗΡΩΝΕΤΑΙ: %] για δικούς του κατοίκους.','Το κτίριο αναβαθμίζεται και αξιοποιείται ξανά.'],
            'Απεικόνιση','κοινόχρηστος χώρος')
        beye, bh = 'Οφέλη για τον δήμο', 'Κοινωνικό έργο, <em>μηδενικό κόστος.</em>'
        benefits = [('Στέγη για τους δικούς σας','Θέσεις για ηλικιωμένους του δήμου που τις έχουν πραγματικά ανάγκη.'),
                    ('Αξιοποίηση ακινήτου','Ένα ανενεργό κτίριο μεταμορφώνεται σε ζωντανή κοινότητα.'),
                    ('Κοινωνικό αποτύπωμα','Μια έμπρακτη λύση για το δημογραφικό και την φροντίδα τρίτης ηλικίας.')]
        cta = ('Είστε δήμος και ενδιαφέρεστε;','Επικοινωνήστε μαζί μας και θα σας παρουσιάσουμε αναλυτικά την πρόταση συνεργασίας.',
               '<a href="contact.html" class="btn btn-primary">Επικοινωνία</a>')
    else:
        H = hero('For Municipalities','A solution for your<br><em>older residents.</em>',
            'The municipality provides a building. We renovate and fit it out. In return, the municipality secures places for its own residents.',
            '<a href="contact.html" class="btn btn-primary">Get in touch</a>',
            'Illustration','municipal building / renovation')
        split = ('The partnership','An agreement <em>that benefits everyone.</em>',
            '<p>Many municipalities have buildings sitting unused — and, at the same time, older residents living in poor conditions. ESTIA connects the two.</p>',
            ['The municipality provides the building — with no capital outlay.','We take on the renovation and the operation.',
             'The municipality receives a share of the places [TO BE COMPLETED: %] for its own residents.','The building is upgraded and put back to use.'],
            'Illustration','a shared space')
        beye, bh = 'Benefits for the municipality', 'Social impact, <em>at zero cost.</em>'
        benefits = [('Housing for your people','Places for the municipality’s older residents who genuinely need them.'),
                    ('Property put to use','A dormant building is transformed into a living community.'),
                    ('Social footprint','A concrete answer to the demographic challenge and elderly care.')]
        cta = ('Are you a municipality and interested?','Get in touch and we will present the partnership proposal in full.',
               '<a href="contact.html" class="btn btn-primary">Contact</a>')
    se, sh, sp, sticks, svl, svs = split
    ticks_html = "".join('            ' + tick(x) + '\n' for x in sticks)
    bcards = "".join(card(CHK, t, d) for t, d in benefits)
    return (H +
     '  <section class="section">\n    <div class="wrap">\n      <div class="split">\n'
     '        <div class="split-text reveal">\n          <p class="eyebrow">' + se + '</p>\n'
     '          <h2 class="h-lg">' + sh + '</h2>\n'
     '          <div class="prose" style="margin-top:1.3rem;">' + sp + '</div>\n'
     '          <ul class="ticks">\n' + ticks_html + '          </ul>\n        </div>\n'
     '        <div class="split-visual reveal">' + ph(svl, svs, "tall") + '</div>\n'
     '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section warm">\n    <div class="wrap">\n' + sechead(beye, bh, center=True) +
     '      <div class="cards">\n' + bcards + '      </div>\n    </div>\n  </section>\n\n' + cta_band(*cta))

def body_expats(lang):
    EL = lang == 'el'
    if EL:
        H = hero('Για Ξένους · Μετακόμιση στην Ελλάδα','Συνταξιοδότηση στην Ελλάδα,<br><em>χωρίς τον πονοκέφαλο.</em>',
            'Ονειρεύεσαι να ζήσεις τα χρόνια της σύνταξης στον ήλιο της Μεσογείου; Σε υποδεχόμαστε σε μια έτοιμη κοινότητα — και αναλαμβάνουμε όλη τη μετακόμιση, από την πρώτη απόφαση μέχρι το κλειδί του δωματίου σου.',
            '<a href="#interest" class="btn btn-primary">Εκδήλωση Ενδιαφέροντος</a> <a href="cohousing.html" class="btn btn-ghost">Δες το μοντέλο</a>',
            'Φωτογραφία','μεσογειακό τοπίο / κοινότητα')
        wye, wh = 'Γιατί η Ελλάδα', 'Ένας τόπος για να <em>ανθίσεις ξανά.</em>'
        why = [(IC_GLOBE,'Μεσογειακή ζωή','Ήλιος, θάλασσα, φρέσκο φαγητό και έναν ρυθμό ζωής που σε κάνει καλά — όλο τον χρόνο.'),
               (IC_HEART,'Χαμηλότερο κόστος','Η καθημερινότητα στην Ελλάδα κοστίζει σημαντικά λιγότερο από τις περισσότερες χώρες της Δύσης.'),
               (IC_USERS,'Έτοιμη κοινότητα','Δεν φτάνεις σε έναν άγνωστο τόπο μόνος. Μπαίνεις κατευθείαν σε μια παρέα ανθρώπων που ταιριάζουν μαζί σου.')]
        rye, rh = 'Υπηρεσίες Μετακόμισης', 'Από την απόφαση, <em>μέχρι το κλειδί.</em>'
        rlead = 'Αναλαμβάνουμε όλη τη διαδικασία και τη γραφειοκρατία, ώστε εσύ να ασχοληθείς μόνο με το ωραίο κομμάτι: τη νέα σου ζωή.'
        steps = [
          ('Πρώτη Γνωριμία','Μια βιντεοκλήση για να καταλάβουμε τι ονειρεύεσαι, τις ανάγκες σου και το χρονοδιάγραμμά σου.'),
          ('Άδεια Διαμονής & Χαρτιά','Σε καθοδηγούμε και σε υποστηρίζουμε σε όλα τα απαραίτητα έγγραφα για να ζήσεις νόμιμα στην Ελλάδα. [ΣΥΜΠΛΗΡΩΝΕΤΑΙ: τι ακριβώς αναλαμβάνουμε.]'),
          ('ΑΦΜ, Τράπεζα & Ασφάλιση','Φορολογικό μητρώο, άνοιγμα τραπεζικού λογαριασμού και πρόσβαση σε υγειονομική κάλυψη — τα τακτοποιούμε μαζί.'),
          ('Μετακόμιση & Μεταφορά','Οργάνωση της μεταφοράς των πραγμάτων σου και όλα τα πρακτικά της εγκατάστασης.'),
          ('Εγκατάσταση & Γνωριμία','Το δωμάτιό σου είναι έτοιμο. Σε συστήνουμε στην κοινότητα και σε βοηθάμε να γνωρίσεις τη γειτονιά σου.'),
          ('Σου δίνουμε το κλειδί','Από εδώ και πέρα, είσαι στο σπίτι σου.'),
        ]
        cye, ch = 'Κοινότητες ξένων', 'Δεν θα είσαι <em>μόνος.</em>'
        cprose = ('<p>Ταιριάζουμε ανθρώπους με κοινή γλώσσα, κουλτούρα και ενδιαφέροντα — ώστε να χτίζονται κοινότητες όπου ο καθένας νιώθει «σαν στο σπίτι του». '
                  'Αν θέλεις, μπορείς να έρθεις μαζί με φίλους ή με μια ομάδα συμπατριωτών σου και να δημιουργήσετε τη δική σας κοινότητα.</p>')
        iye, ih = 'Εκδήλωση Ενδιαφέροντος', 'Πες μας <em>για σένα.</em>'
        ilead = 'Άφησε τα στοιχεία σου και θα επικοινωνήσουμε μαζί σου — στη γλώσσα σου.'
    else:
        H = hero('For Expats · Relocating to Greece','Retire in Greece,<br><em>without the headache.</em>',
            'Dreaming of spending your retirement years in the Mediterranean sun? We welcome you into a ready-made community — and we handle the whole move, from your first decision to the key to your room.',
            '<a href="#interest" class="btn btn-primary">Register Your Interest</a> <a href="cohousing.html" class="btn btn-ghost">See the model</a>',
            'Photo','Mediterranean landscape / community')
        wye, wh = 'Why Greece', 'A place to <em>blossom again.</em>'
        why = [(IC_GLOBE,'Mediterranean life','Sun, sea, fresh food and a pace of life that does you good — all year round.'),
               (IC_HEART,'A lower cost of living','Everyday life in Greece costs significantly less than in most Western countries.'),
               (IC_USERS,'A ready-made community','You do not arrive in a strange place alone. You step straight into a circle of people who fit with you.')]
        rye, rh = 'Relocation Services', 'From the decision, <em>to the key.</em>'
        rlead = 'We take on the entire process and the paperwork, so that you only have to deal with the good part: your new life.'
        steps = [
          ('First Conversation','A video call to understand what you are dreaming of, your needs and your timeline.'),
          ('Residence Permit & Paperwork','We guide and support you through all the documents you need to live in Greece legally. [TO BE COMPLETED: exactly what we handle.]'),
          ('Tax ID, Bank & Insurance','Tax registration, opening a bank account and access to healthcare cover — we sort them out together.'),
          ('Moving & Shipping','Organising the shipping of your belongings and all the practicalities of settling in.'),
          ('Settling In & Introductions','Your room is ready. We introduce you to the community and help you get to know your neighbourhood.'),
          ('We hand you the key','From here on, you are home.'),
        ]
        cye, ch = 'Expat communities', 'You will not be <em>on your own.</em>'
        cprose = ('<p>We match people who share a language, a culture and interests — so that communities form where everyone feels at home. '
                  'If you like, you can come together with friends or a group of fellow nationals and create a community of your own.</p>')
        iye, ih = 'Register Your Interest', 'Tell us <em>about you.</em>'
        ilead = 'Leave your details and we will get in touch — in your language.'
    # why cards
    why_cards = "".join(card(ic, t, d) for ic, t, d in why)
    # steps
    steps_html = ""
    for i, (t, d) in enumerate(steps, 1):
        steps_html += '        <div class="step reveal"><div class="step-num">' + str(i) + '</div><div><h3>' + t + '</h3><p>' + d + '</p></div></div>\n'
    form = expats_form(lang)
    return (H +
     '  <section class="section">\n    <div class="wrap">\n' + sechead(wye, wh, center=True) +
     '      <div class="cards">\n' + why_cards + '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section warm">\n    <div class="wrap">\n' + sechead(rye, rh, rlead) +
     '      <div class="steps">\n' + steps_html + '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section">\n    <div class="wrap">\n      <div class="split">\n'
     '        <div class="split-text reveal">\n          <p class="eyebrow">' + cye + '</p>\n'
     '          <h2 class="h-lg">' + ch + '</h2>\n'
     '          <div class="prose" style="margin-top:1.3rem;">' + cprose + '</div>\n        </div>\n'
     '        <div class="split-visual reveal">' + ph(('Φωτογραφία' if EL else 'Photo'), ('παρέα / κοινότητα' if EL else 'friends / community'), "tall") + '</div>\n'
     '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section cream" id="interest">\n    <div class="wrap">\n' + sechead(iye, ih, ilead) + form +
     '    </div>\n  </section>\n\n')

def body_about(lang):
    EL = lang == 'el'
    if EL:
        H = hero('Η Ομάδα μας','Ποιοι<br><em>Είμαστε.</em>',
            'Δύο φίλοι με μια κοινή πεποίθηση: ότι τα χρόνια μετά τα 60 μπορούν να είναι τα πιο ουσιαστικά.',
            '<a href="contact.html" class="btn btn-primary">Επικοινωνία</a>',
            'Φωτογραφία','η ομάδα / οι ιδρυτές')
        se, sh = 'Πώς ξεκινήσαμε', 'Από μια απλή <em>διαπίστωση.</em>'
        sp = '<p>[ΣΥΜΠΛΗΡΩΝΕΤΑΙ: η ιστορία της ΕΣΤΙΑ — πώς ξεκίνησε η ιδέα, τι σας έδωσε το έναυσμα, ποιος άνθρωπος ή στιγμή έκανε τη διαφορά.]</p>'
        svl, svs = 'Φωτογραφία','η αρχή της ιδέας'
        vye, vh = 'Οι αξίες μας', 'Αυτά που <em>δεν διαπραγματευόμαστε.</em>'
        values = [('Σύνδεση','Πιστεύουμε ότι η μοναξιά είναι η μεγαλύτερη απειλή — και η σύνδεση το αντίδοτό της.'),
                  ('Αυτονομία','Σχεδιάζουμε για να κάνει ο κάθε άνθρωπος τα πράγματα μόνος του. Η αξιοπρέπεια πηγάζει από την ανεξαρτησία.'),
                  ('Αξιοπρέπεια','Κάθε κάτοικος είναι μέλος μιας κοινότητας — όχι ασθενής, όχι νούμερο.')]
        vnote = '[ΣΥΜΠΛΗΡΩΝΕΤΑΙ: η τελική διατύπωση των αξιών — αν θέλετε διαφορετικές ή περισσότερες.]'
        tye, th = 'Η ομάδα μας', 'Οι άνθρωποι <em>πίσω από την ΕΣΤΙΑ.</em>'
        team = [('[Όνομα]','Συν-ιδρυτής','[Σύντομο βιογραφικό.]'),('[Όνομα]','Συν-ιδρυτής','[Σύντομο βιογραφικό.]'),('[Όνομα]','[Ρόλος]','[Σύντομο βιογραφικό.]')]
        cta = ('Έλα στην ομάδα μας','Χτίζουμε κάτι καινούργιο για την Ελλάδα. Αν μοιράζεσαι το όραμά μας, θα χαρούμε να σε γνωρίσουμε.',
               '<a href="careers.html" class="btn btn-primary">Δες τις θέσεις μας</a>')
    else:
        H = hero('Our Team','Who<br><em>We Are.</em>',
            'Two friends with one shared belief: that the years after 60 can be the most meaningful of all.',
            '<a href="contact.html" class="btn btn-primary">Contact</a>',
            'Photo','the team / the founders')
        se, sh = 'How we started', 'From a simple <em>realisation.</em>'
        sp = '<p>[TO BE COMPLETED: the story of ESTIA — how the idea began, what sparked it, which person or moment made the difference.]</p>'
        svl, svs = 'Photo','the beginning of the idea'
        vye, vh = 'Our values', 'The things we <em>will not compromise on.</em>'
        values = [('Connection','We believe loneliness is the greatest threat — and connection is its antidote.'),
                  ('Autonomy','We design so that each person can do things for themselves. Dignity flows from independence.'),
                  ('Dignity','Every resident is a member of a community — not a patient, not a number.')]
        vnote = '[TO BE COMPLETED: the final wording of the values — if you want different or additional ones.]'
        tye, th = 'Our team', 'The people <em>behind ESTIA.</em>'
        team = [('[Name]','Co-founder','[Short bio.]'),('[Name]','Co-founder','[Short bio.]'),('[Name]','[Role]','[Short bio.]')]
        cta = ('Join our team','We are building something new for Greece. If you share our vision, we would love to meet you.',
               '<a href="careers.html" class="btn btn-primary">See our open roles</a>')
    vpills = "".join('        <div class="pillar reveal"><h3>' + t + '</h3><p>' + d + '</p></div>\n' for t, d in values)
    members = ""
    for n, r, b in team:
        members += '        <div class="member reveal">' + ph('Φωτογραφία' if EL else 'Photo') + '<h3>' + n + '</h3><p class="role">' + r + '</p><p>' + b + '</p></div>\n'
    return (H +
     '  <section class="section">\n    <div class="wrap">\n      <div class="split">\n'
     '        <div class="split-text reveal"><p class="eyebrow">' + se + '</p>\n'
     '          <h2 class="h-lg">' + sh + '</h2>\n'
     '          <div class="prose" style="margin-top:1.3rem;">' + sp + '</div>\n        </div>\n'
     '        <div class="split-visual reveal">' + ph(svl, svs, "tall") + '</div>\n'
     '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section warm">\n    <div class="wrap">\n' + sechead(vye, vh) +
     '      <div class="pillars">\n' + vpills + '      </div>\n'
     '      <div class="callout reveal" style="margin-top:2.5rem;"><p>' + vnote + '</p></div>\n'
     '    </div>\n  </section>\n\n'
     '  <section class="section">\n    <div class="wrap">\n' + sechead(tye, th, center=True) +
     '      <div class="team">\n' + members + '      </div>\n    </div>\n  </section>\n\n' + cta_band(*cta))

def body_careers(lang):
    EL = lang == 'el'
    if EL:
        H = hero('Καριέρα','Χτίζουμε κάτι καινούργιο.<br><em>Έλα μαζί μας.</em>',
            'Η ΕΣΤΙΑ φέρνει στην Ελλάδα ένα μοντέλο που αλλάζει τη ζωή ανθρώπων. Ψάχνουμε ανθρώπους που θέλουν να φτιάξουν κάτι ουσιαστικό από την αρχή — όχι απλώς μια δουλειά.',
            '<a href="#positions" class="btn btn-primary">Δες τις θέσεις</a> <a href="about.html" class="btn btn-ghost">Ποιοι Είμαστε</a>',
            'Φωτογραφία','η ομάδα σε δράση')
        wye, wh = 'Γιατί ΕΣΤΙΑ', 'Μια δουλειά <em>με νόημα.</em>'
        why = [(IC_HEART,'Πραγματικός αντίκτυπος','Η δουλειά σου βελτιώνει άμεσα την καθημερινότητα πραγματικών ανθρώπων.'),
               (IC_SEED,'Από το μηδέν','Μπαίνεις νωρίς, με λόγο στις αποφάσεις και χώρο να μεγαλώσεις μαζί με την εταιρία.'),
               (IC_ROCKET,'Ομάδα που μαθαίνει','Μικρή, φιλόδοξη ομάδα που δοκιμάζει, μαθαίνει γρήγορα και στηρίζει ο ένας τον άλλον.')]
        pye, ph_h = 'Ανοιχτές θέσεις', 'Ποιους <em>ψάχνουμε τώρα.</em>'
        jobs = [
          ('Υπεύθυνος/η Κοινότητας & Λειτουργίας','Πλήρης απασχόληση','Αθήνα',
           'Είσαι το ανθρώπινο πρόσωπο της ΕΣΤΙΑ — φροντίζεις ώστε κάθε κοινότητα να λειτουργεί αρμονικά και κάθε κάτοικος να νιώθει σαν στο σπίτι του.',
           ['Υποδοχή και ένταξη (onboarding) των νέων κατοίκων.','Καθημερινή λειτουργία και συντονισμός των υπηρεσιών (καθαριότητα, γιατρός, συντήρηση).',
            'Υποστήριξη του ταιριάσματος συγκατοίκων και της ζωής της κοινότητας.','Επίλυση ζητημάτων, διαμεσολάβηση και οργάνωση δραστηριοτήτων.'],
           ['Εμπειρία σε community management, hospitality, φροντίδα ή διαχείριση.','Εξαιρετική επικοινωνία, ενσυναίσθηση και οργανωτικότητα.',
            'Άνεση και σεβασμός στη σχέση με ανθρώπους 60+.','Άριστα ελληνικά και καλά αγγλικά.']),
          ('Υπεύθυνος/η Ανάπτυξης & Συνεργασιών','Πλήρης απασχόληση','Αθήνα',
           'Ανοίγεις πόρτες — βρίσκεις ακίνητα, χτίζεις συνεργασίες με δήμους και επενδυτές, και φέρνεις τους πρώτους κατοίκους.',
           ['Εντοπισμός και αξιολόγηση κατάλληλων ακινήτων.','Συνεργασίες με δήμους, φορείς και επενδυτές.',
            'Lead generation, marketing και χτίσιμο του pipeline κατοίκων (συμπ. ξένων συνταξιούχων).','Διαπραγματεύσεις και διαχείριση σχέσεων.'],
           ['Εμπειρία σε business development, sales, partnerships ή real estate.','Δίκτυο επαφών και άνεση στη διαπραγμάτευση.',
            'Προσανατολισμός στο αποτέλεσμα και αυτονομία.','Άριστα ελληνικά και αγγλικά.']),
          ('Μηχανικός Λογισμικού (Full-Stack) — Πλατφόρμα & Ταίριασμα','Πλήρης απασχόληση','Αθήνα / Remote',
           'Χτίζεις την τεχνολογική καρδιά της ΕΣΤΙΑ: το λογισμικό ταιριάσματος, την πλατφόρμα ενημέρωσης και αναφοράς, και τον αλγόριθμο επιλογής περιοχής.',
           ['Σχεδιασμός και ανάπτυξη του λογισμικού ταιριάσματος ανθρώπων.','Πλατφόρμα κεντρικής ενημέρωσης και αναφοράς παραπόνων.',
            'Αλγόριθμος επιλογής περιοχής με βάση τις ανάγκες των ενδιαφερομένων.','Ανάπτυξη end-to-end (frontend + backend), με σεβασμό στα δεδομένα και την ιδιωτικότητα.'],
           ['Σταθερή εμπειρία full-stack (π.χ. JavaScript/TypeScript, Python, SQL).','Καθαρός κώδικας και προϊοντική σκέψη.',
            'Όρεξη για 0→1 ανάπτυξη σε περιβάλλον startup.','Ελληνικά ή/και αγγλικά.']),
        ]
        resp_t, req_t = 'Τι θα κάνεις', 'Τι ψάχνουμε'
        apply_t = 'Κάνε αίτηση'
        note = ('Δεν βρίσκεις τη θέση που σου ταιριάζει; Στείλε μας το βιογραφικό σου στο '
                '<a href="mailto:estia.cohousing@gmail.com">estia.cohousing@gmail.com</a> — πάντα ψάχνουμε ξεχωριστούς ανθρώπους.')
        cta = ('Σε ενδιαφέρει;','Στείλε μας το βιογραφικό σου και δυο λόγια για το ποιος είσαι.',
               '<a href="mailto:estia.cohousing@gmail.com?subject=' + urllib.parse.quote('Αίτηση για θέση στην ΕΣΤΙΑ') + '" class="btn btn-primary">Στείλε βιογραφικό</a> <a href="about.html" class="btn btn-ghost">Ποιοι Είμαστε</a>')
    else:
        H = hero('Careers','We are building something new.<br><em>Come build it with us.</em>',
            'ESTIA is bringing a life-changing model to Greece. We are looking for people who want to build something meaningful from the ground up — not just take a job.',
            '<a href="#positions" class="btn btn-primary">See the roles</a> <a href="about.html" class="btn btn-ghost">About Us</a>',
            'Photo','the team at work')
        wye, wh = 'Why ESTIA', 'Work <em>that matters.</em>'
        why = [(IC_HEART,'Real impact','Your work directly improves the everyday lives of real people.'),
               (IC_SEED,'From the ground up','You join early, with a say in decisions and room to grow with the company.'),
               (IC_ROCKET,'A team that learns','A small, ambitious team that experiments, learns fast and has each other’s backs.')]
        pye, ph_h = 'Open roles', 'Who we are <em>hiring now.</em>'
        jobs = [
          ('Community & Operations Manager','Full-time','Athens',
           'You are the human face of ESTIA — making sure each community runs smoothly and every resident feels at home.',
           ['Welcoming and onboarding new residents.','Day-to-day operations and coordinating services (cleaning, doctor, maintenance).',
            'Supporting housemate matching and the life of the community.','Resolving issues, mediating, and organising activities.'],
           ['Experience in community management, hospitality, care or operations.','Excellent communication, empathy and organisation.',
            'Comfort and respect in working with people aged 60+.','Fluent Greek and good English.']),
          ('Partnerships & Growth Lead','Full-time','Athens',
           'You open doors — finding properties, building relationships with municipalities and investors, and bringing in the first residents.',
           ['Identifying and evaluating suitable properties.','Partnerships with municipalities, public bodies and investors.',
            'Lead generation, marketing and building the resident pipeline (including foreign retirees).','Negotiation and relationship management.'],
           ['Experience in business development, sales, partnerships or real estate.','A network of contacts and comfort with negotiation.',
            'Results-driven and self-directed.','Fluent Greek and English.']),
          ('Full-Stack Software Engineer — Platform & Matching','Full-time','Athens / Remote',
           'You build the technological heart of ESTIA: the matching software, the information & reporting platform, and the location-selection algorithm.',
           ['Designing and building the people-matching software.','A central information and complaint-reporting platform.',
            'A location-selection algorithm based on the needs of interested people.','End-to-end development (frontend + backend), with respect for data and privacy.'],
           ['Solid full-stack experience (e.g. JavaScript/TypeScript, Python, SQL).','Clean code and product thinking.',
            'Appetite for 0→1 building in a startup environment.','Greek and/or English.']),
        ]
        resp_t, req_t = 'What you’ll do', 'What we’re looking for'
        apply_t = 'Apply'
        note = ('Don’t see the role that fits you? Send us your CV at '
                '<a href="mailto:estia.cohousing@gmail.com">estia.cohousing@gmail.com</a> — we are always looking for exceptional people.')
        cta = ('Interested?','Send us your CV and a few words about who you are.',
               '<a href="mailto:estia.cohousing@gmail.com?subject=' + urllib.parse.quote('Application for a role at ESTIA') + '" class="btn btn-primary">Send your CV</a> <a href="about.html" class="btn btn-ghost">About Us</a>')
    why_cards = "".join(card(ic, t, d) for ic, t, d in why)
    jobs_html = ""
    for title, jtype, loc, intro, resp, req in jobs:
        resp_li = "".join('            ' + tick(x) + '\n' for x in resp)
        req_li = "".join('            ' + tick(x) + '\n' for x in req)
        jobs_html += (
          '        <div class="job reveal">\n'
          '          <div class="job-head">\n'
          '            <h3>' + title + '</h3>\n'
          '            <div class="job-tags"><span>' + jtype + '</span><span>' + loc + '</span></div>\n'
          '          </div>\n'
          '          <p class="job-intro">' + intro + '</p>\n'
          '          <div class="job-cols">\n'
          '            <div><h4>' + resp_t + '</h4><ul class="ticks">\n' + resp_li + '            </ul></div>\n'
          '            <div><h4>' + req_t + '</h4><ul class="ticks">\n' + req_li + '            </ul></div>\n'
          '          </div>\n'
          '          <a href="' + mailto(title, lang) + '" class="btn btn-primary">' + apply_t + '</a>\n'
          '        </div>\n')
    return (H +
     '  <section class="section">\n    <div class="wrap">\n' + sechead(wye, wh, center=True) +
     '      <div class="cards">\n' + why_cards + '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section warm" id="positions">\n    <div class="wrap">\n' + sechead(pye, ph_h) +
     '      <div class="jobs">\n' + jobs_html + '      </div>\n'
     '      <div class="callout reveal" style="margin-top:2.5rem;"><p>' + note + '</p></div>\n'
     '    </div>\n  </section>\n\n' + cta_band(*cta))

def post_cards(lang, kind, meta, titles):
    EL = lang == 'el'
    summ = '[Σύντομη περίληψη — συμπληρώνεται.]' if EL else '[Short summary — to be completed.]'
    out = ""
    for mt, ti in zip(meta, titles):
        out += ('        <a href="#" class="post reveal">' + ph(kind) +
                '<div class="post-body"><p class="post-meta">' + mt + '</p><h3>' + ti + '</h3><p>' + summ + '</p></div></a>\n')
    return out

def body_news(lang):
    EL = lang == 'el'
    if EL:
        eye, h = 'Ενημέρωση', 'Νέα<br><em>της ΕΣΤΙΑ.</em>'
        lead = 'Ανακοινώσεις, ορόσημα και εξελίξεις από την ομάδα μας.'
        meta = ['[Ημερομηνία]','[Ημερομηνία]','[Ημερομηνία]']
        titles = ['[Τίτλος νέου 1]','[Τίτλος νέου 2]','[Τίτλος νέου 3]']
        kind = 'Εικόνα νέου'
        note = 'Σύντομα τα πρώτα μας νέα. [ΣΥΜΠΛΗΡΩΝΟΝΤΑΙ οι ανακοινώσεις της εταιρίας.]'
    else:
        eye, h = 'Updates', 'News<br><em>from ESTIA.</em>'
        lead = 'Announcements, milestones and developments from our team.'
        meta = ['[Date]','[Date]','[Date]']
        titles = ['[News title 1]','[News title 2]','[News title 3]']
        kind = 'News image'
        note = 'Our first news is coming soon. [Company announcements to be added.]'
    return ('  <section class="section" style="padding-top:4rem;">\n    <div class="wrap">\n' +
     sechead(eye, h, lead, size="h-xl") +
     '      <div class="posts">\n' + post_cards(lang, kind, meta, titles) + '      </div>\n'
     '      <div class="callout reveal" style="margin-top:2.5rem;"><p>' + note + '</p></div>\n'
     '    </div>\n  </section>\n\n')

def body_blog(lang):
    EL = lang == 'el'
    if EL:
        eye, h = 'Ενημέρωση', 'Blog &<br><em>Συμβουλές.</em>'
        lead = 'Άρθρα και συμβουλές για τους κατοίκους, αλλά και για όσους αναζητούν τη ζωή σε κοινότητα.'
        meta = ['Συμβουλές διαβίωσης','Για τις κοινότητες','Υγεία & Ευεξία']
        titles = ['[Τίτλος άρθρου 1]','[Τίτλος άρθρου 2]','[Τίτλος άρθρου 3]']
        kind = 'Εικόνα άρθρου'
        note = 'Εδώ θα ανεβάσουμε τα άρθρα από τη σελίδα μας στο Facebook και νέα άρθρα. [ΣΥΜΠΛΗΡΩΝΟΝΤΑΙ τα άρθρα.]'
    else:
        eye, h = 'Updates', 'Blog &<br><em>Tips.</em>'
        lead = 'Articles and advice for residents, and for anyone seeking life in community.'
        meta = ['Living tips','On communities','Health & Wellbeing']
        titles = ['[Article title 1]','[Article title 2]','[Article title 3]']
        kind = 'Article image'
        note = 'Here we will post the articles from our Facebook page, along with new ones. [Articles to be added.]'
    return ('  <section class="section" style="padding-top:4rem;">\n    <div class="wrap">\n' +
     sechead(eye, h, lead, size="h-xl") +
     '      <div class="posts">\n' + post_cards(lang, kind, meta, titles) + '      </div>\n'
     '      <div class="callout reveal" style="margin-top:2.5rem;"><p>' + note + '</p></div>\n'
     '    </div>\n  </section>\n\n')

def interest_options(lang, expats=False):
    EL = lang == 'el'
    if EL:
        opts = [('','Επίλεξε...'),('resident','Για τον εαυτό μου'),('family','Για μέλος της οικογένειάς μου'),
                ('relocation','Μετακόμιση από το εξωτερικό'),('investor','Ως επενδυτής'),
                ('municipality','Ως δήμος'),('careers','Για δουλειά / καριέρα'),('other','Άλλο')]
    else:
        opts = [('','Choose...'),('resident','For myself'),('family','For a family member'),
                ('relocation','Relocating from abroad'),('investor','As an investor'),
                ('municipality','As a municipality'),('careers','A job / career'),('other','Other')]
    return "".join('<option value="' + v + '">' + l + '</option>' for v, l in opts)

def contact_form(lang, action_note=True):
    EL = lang == 'el'
    if EL:
        l_name, ph_name = 'Ονοματεπώνυμο', 'Αθανάσιος Παπαδόπουλος'
        l_age = 'Ηλικία'; l_phone = 'Τηλέφωνο'; ph_phone = '+30 69X XXX XXXX'
        l_email = 'Email (προαιρετικό)'; l_int = 'Πώς σε ενδιαφέρει;'
        l_msg = 'Σχόλια ή ερωτήσεις'; ph_msg = 'Πες μας τι σε ενδιαφέρει περισσότερο...'
        note = 'Τα στοιχεία σου χρησιμοποιούνται αποκλειστικά για επικοινωνία σχετικά με το πρόγραμμα ΕΣΤΙΑ. Δεν τα κοινοποιούμε σε τρίτους.'
        submit = 'Αποστολή Στοιχείων'
        ok_h, ok_p = 'Ευχαριστούμε!', 'Θα επικοινωνήσουμε μαζί σου σύντομα.'
    else:
        l_name, ph_name = 'Full name', 'John Smith'
        l_age = 'Age'; l_phone = 'Phone'; ph_phone = '+30 69X XXX XXXX'
        l_email = 'Email (optional)'; l_int = 'How are you interested?'
        l_msg = 'Comments or questions'; ph_msg = 'Tell us what interests you most...'
        note = 'Your details are used solely to contact you about the ESTIA programme. We never share them with third parties.'
        submit = 'Send My Details'
        ok_h, ok_p = 'Thank you!', 'We will be in touch soon.'
    return (
     '        <div class="reveal">\n'
     '          <form class="form" id="contactForm" action="https://formspree.io/f/mgonorkv" method="POST">\n'
     '            <div class="form-row">\n'
     '              <div class="field"><label for="name">' + l_name + '</label><input type="text" id="name" name="name" placeholder="' + ph_name + '" required></div>\n'
     '              <div class="field"><label for="age">' + l_age + '</label><input type="number" id="age" name="age" placeholder="65" min="55" max="95"></div>\n'
     '            </div>\n'
     '            <div class="form-row">\n'
     '              <div class="field"><label for="phone">' + l_phone + '</label><input type="tel" id="phone" name="phone" placeholder="' + ph_phone + '" required></div>\n'
     '              <div class="field"><label for="email">' + l_email + '</label><input type="email" id="email" name="email" placeholder="email@example.com"></div>\n'
     '            </div>\n'
     '            <div class="field"><label for="interest">' + l_int + '</label><select id="interest" name="interest">' + interest_options(lang) + '</select></div>\n'
     '            <div class="field"><label for="message">' + l_msg + '</label><textarea id="message" name="message" placeholder="' + ph_msg + '"></textarea></div>\n'
     '            <input type="text" name="_gotcha" style="display:none">\n'
     '            <input type="hidden" name="_language" value="' + lang + '">\n'
     '            <p class="form-note">' + note + '</p>\n'
     '            <button type="submit" class="submit-btn">' + submit + '</button>\n'
     '          </form>\n'
     '          <div class="success-msg" id="successMsg"><h3>' + ok_h + '</h3><p>' + ok_p + '</p></div>\n'
     '        </div>\n')

def expats_form(lang):
    # a focused variant reusing the same form component
    return '      <div class="contact-grid" style="grid-template-columns:1fr;max-width:760px;margin:0 auto;">\n' + contact_form(lang) + '      </div>\n'

def body_contact(lang):
    EL = lang == 'el'
    if EL:
        eye, h = 'Επικοινωνία', 'Ας τα πούμε<br><em>από κοντά.</em>'
        info_h = 'Θα χαρούμε να σε ακούσουμε.'
        info_p = 'Άφησε τα στοιχεία σου και θα επικοινωνήσουμε μαζί σου για να σου εξηγήσουμε το μοντέλο, το κόστος και τις διαθέσιμες θέσεις.'
        phone_t = '[Τηλέφωνο — συμπληρώνεται]'; loc_t = 'Αθήνα, Ελλάδα'
    else:
        eye, h = 'Contact', "Let's talk<br><em>in person.</em>"
        info_h = 'We would love to hear from you.'
        info_p = 'Leave your details and we will get in touch to walk you through the model, the cost and the available places.'
        phone_t = '[Phone — to be added]'; loc_t = 'Athens, Greece'
    return ('  <section class="section" style="padding-top:4rem;">\n    <div class="wrap">\n' +
     sechead(eye, h, size="h-xl") +
     '      <div class="contact-grid">\n'
     '        <div class="contact-info reveal">\n'
     '          <h3>' + info_h + '</h3>\n'
     '          <p style="color:var(--muted);line-height:1.8;margin-bottom:1.5rem;">' + info_p + '</p>\n'
     '          <a href="mailto:estia.cohousing@gmail.com" class="info-row">' + IC_MAIL + ' estia.cohousing@gmail.com</a>\n'
     '          <div class="info-row">' + IC_PHONE + ' ' + phone_t + '</div>\n'
     '          <div class="info-row">' + IC_PIN + ' ' + loc_t + '</div>\n'
     '        </div>\n' + contact_form(lang) +
     '      </div>\n    </div>\n  </section>\n\n')

def body_history(lang):
    EL = lang == 'el'
    def tl(year, text):
        return '        <div class="tl-item reveal"><div class="tl-year">' + year + '</div><div class="tl-text">' + text + '</div></div>\n'
    if EL:
        H = hero('Συστέγαση / Co-Housing','Ιστορία του<br><em>Cohousing.</em>',
            'Μια ιδέα με περισσότερα από πενήντα χρόνια ζωής — από τη Δανία του 1972 μέχρι τις σύγχρονες κοινότητες σε όλο τον κόσμο.',
            '<a href="research.html" class="btn btn-primary">Έρευνες & Τεκμηρίωση</a> <a href="cohousing.html" class="btn btn-ghost">Το μοντέλο μας</a>',
            'Απεικόνιση','κοινότητα cohousing')
        s1e, s1h = 'Τι είναι', 'Ιδιωτικότητα και κοινότητα, <em>μαζί.</em>'
        s1p = ('<p>Ο όρος Συστέγαση / Cohousing περιγράφει έναν σύγχρονο τρόπο κατοίκησης που συνδυάζει την ιδιωτικότητα ενός ανεξάρτητου σπιτιού με τα οφέλη μιας μικρής, ενεργής κοινότητας. Κάθε κάτοικος διατηρεί τον προσωπικό του χώρο και την ανεξαρτησία του, ενώ παράλληλα μοιράζεται κοινόχρηστους χώρους και στιγμές της καθημερινότητας.</p>'
               '<p>Δεν πρόκειται για συγκατοίκηση, ούτε για μονάδα φροντίδας — αλλά για μια διαφορετική φιλοσοφία κατοίκησης, βασισμένη στην ελευθερία επιλογής και την αμοιβαία υποστήριξη.</p>')
        s2e, s2h = 'Από πού ξεκίνησε', 'Δανία, τέλη δεκαετίας <em>του 1960.</em>'
        tls = [('1960s','Οικογένειες στη Δανία αναζητούν έναν τρόπο ζωής που κρατά την ιδιωτικότητα του σπιτιού, χωρίς να χάνεται η καθημερινή ανθρώπινη επαφή.'),
               ('1972','Δημιουργείται η πρώτη οργανωμένη κοινότητα Cohousing έξω από την Κοπεγχάγη. Το μοντέλο εξαπλώνεται σε όλη τη Βόρεια Ευρώπη.'),
               ('Σήμερα','Μια ώριμη μορφή κατοίκησης με περισσότερα από 50 χρόνια εξέλιξης, διαδεδομένη σε πολλές χώρες του κόσμου.')]
        s3e, s3h = 'Senior Cohousing', 'Αυτονομία, χωρίς <em>απομόνωση.</em>'
        s3p = '<p>Με την αύξηση του προσδόκιμου ζωής, όλο και περισσότεροι άνθρωποι μετά τα 60 αναζήτησαν έναν τρόπο να συνεχίσουν να ζουν αυτόνομα, χωρίς να απομακρύνονται από την κοινωνική ζωή. Έτσι γεννήθηκε το Senior Cohousing. Σήμερα λειτουργούν εκατοντάδες τέτοιες κοινότητες στην Ευρώπη και τη Βόρεια Αμερική.</p>'
        reasons = ['Αυξάνεται το προσδόκιμο ζωής.','Ολοένα περισσότερα νοικοκυριά αποτελούνται από ένα ή δύο άτομα.',
                   'Αυξάνεται η ανάγκη για ουσιαστικές ανθρώπινες σχέσεις.','Αυξάνεται το κόστος κατοικίας.',
                   'Ολοένα περισσότεροι επιλέγουν ποιότητα ζωής με λιγότερη απομόνωση.']
        p4e, p4h = 'Παραδείγματα από τον κόσμο', 'Δοκιμασμένο, <em>εδώ και δεκαετίες.</em>'
        projs = [('Ισπανία','Trabensol','Κοινότητα senior cohousing κοντά στη Μαδρίτη, βασισμένη σε συνεταιριστικό μοντέλο και βιώσιμο σχεδιασμό.','https://trabensol.org/','Δες το έργο'),
                 ('Ηνωμένο Βασίλειο','Cannock Mill','Σύγχρονη κοινότητα cohousing στο Colchester, με έμφαση στην ενεργειακή αποδοτικότητα.','https://cannockmillcohousing.co.uk/','Δες το έργο'),
                 ('Διεθνώς','Cohousing Company','Πρωτοπόροι του μοντέλου, με δεκάδες κοινότητες σε πολλές χώρες.','https://www.cohousingco.com/','Δες το έργο')]
        g5e, g5h = 'Γιατί τώρα στην Ελλάδα', 'Η σειρά της <em>Ελλάδας, τώρα.</em>'
        g5p = '<p>Η σύγχρονη αυτή μορφή διαβίωσης έρχεται και στην Ελλάδα. Παρότι το Cohousing είναι διαδεδομένο στο εξωτερικό εδώ και πάνω από 50 χρόνια, στην Ελλάδα βρίσκεται ακόμη στα πρώτα του βήματα. Η ΕΣΤΙΑ δημιουργήθηκε για να φέρει αυτή τη διεθνώς δοκιμασμένη ιδέα στη χώρα μας, προσαρμοσμένη στις ανάγκες και την κουλτούρα της ελληνικής κοινωνίας.</p>'
        cta = ('Μάθε περισσότερα','Δες τι δείχνουν οι διεθνείς μελέτες, ή το δικό μας μοντέλο.',
               '<a href="research.html" class="btn btn-primary">Έρευνες & Τεκμηρίωση</a> <a href="cohousing.html" class="btn btn-ghost">Το μοντέλο μας</a>')
    else:
        H = hero('Co-Housing','History of<br><em>Cohousing.</em>',
            'An idea more than fifty years in the making — from 1972 Denmark to modern communities across the world.',
            '<a href="research.html" class="btn btn-primary">Research & Evidence</a> <a href="cohousing.html" class="btn btn-ghost">Our model</a>',
            'Illustration','a cohousing community')
        s1e, s1h = 'What it is', 'Privacy and community, <em>together.</em>'
        s1p = ('<p>Cohousing describes a modern way of living that combines the privacy of an independent home with the benefits of a small, active community. Each resident keeps their own space and independence, while sharing common areas and everyday moments.</p>'
               '<p>It is neither a flatshare nor a care facility — but a different philosophy of living, built on freedom of choice and mutual support.</p>')
        s2e, s2h = 'Where it began', 'Denmark, the late <em>1960s.</em>'
        tls = [('1960s','Families in Denmark look for a way of living that keeps the privacy of a home without losing daily human contact.'),
               ('1972','The first organised Cohousing community is created outside Copenhagen. The model spreads across Northern Europe.'),
               ('Today','A mature form of living with more than 50 years of development, found in many countries around the world.')]
        s3e, s3h = 'Senior Cohousing', 'Autonomy, without <em>isolation.</em>'
        s3p = '<p>As life expectancy rose, more and more people past 60 sought a way to keep living independently without stepping away from social life. So Senior Cohousing was born. Today there are hundreds of such communities across Europe and North America.</p>'
        reasons = ['Life expectancy is rising.','More and more households are made up of one or two people.',
                   'The need for meaningful human relationships is growing.','The cost of housing is rising.',
                   'More and more people are choosing quality of life with less isolation.']
        p4e, p4h = 'Examples from around the world', 'Proven, <em>for decades.</em>'
        projs = [('Spain','Trabensol','A senior cohousing community near Madrid, built on a cooperative model and sustainable design.','https://trabensol.org/','View the project'),
                 ('United Kingdom','Cannock Mill','A modern cohousing community in Colchester, with a focus on energy efficiency.','https://cannockmillcohousing.co.uk/','View the project'),
                 ('International','Cohousing Company','Pioneers of the model, with dozens of communities in many countries.','https://www.cohousingco.com/','View the project')]
        g5e, g5h = 'Why now in Greece', "It is Greece's <em>turn, now.</em>"
        g5p = '<p>This modern form of living is now coming to Greece. Although Cohousing has been widespread abroad for over 50 years, in Greece it is still taking its first steps. ESTIA was created to bring this internationally tested idea to our country, adapted to the needs and culture of Greek society.</p>'
        cta = ('Learn more','See what the international studies show, or our own model.',
               '<a href="research.html" class="btn btn-primary">Research & Evidence</a> <a href="cohousing.html" class="btn btn-ghost">Our model</a>')
    tl_html = "".join(tl(y, t) for y, t in tls)
    reason_html = "".join('        <li>' + r + '</li>\n' for r in reasons)
    proj_html = ""
    for loc, name, desc, link, label in projs:
        proj_html += ('        <div class="proj reveal"><span class="loc">' + loc + '</span><h3>' + name + '</h3><p>' + desc +
                      '</p><a href="' + link + '" target="_blank" rel="noopener noreferrer">' + label + ' →</a></div>\n')
    return (H +
     '  <section class="section">\n    <div class="wrap">\n' + sechead(s1e, s1h) +
     '      <div class="prose reveal">' + s1p + '</div>\n    </div>\n  </section>\n\n'
     '  <section class="section warm">\n    <div class="wrap">\n' + sechead(s2e, s2h) +
     '      <div class="timeline">\n' + tl_html + '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section">\n    <div class="wrap">\n' + sechead(s3e, s3h) +
     '      <div class="prose reveal">' + s3p + '</div>\n'
     '      <ul class="reason-list reveal">\n' + reason_html + '      </ul>\n    </div>\n  </section>\n\n'
     '  <section class="section cream">\n    <div class="wrap">\n' + sechead(p4e, p4h) +
     '      <div class="proj-grid">\n' + proj_html + '      </div>\n    </div>\n  </section>\n\n'
     '  <section class="section">\n    <div class="wrap">\n' + sechead(g5e, g5h) +
     '      <div class="prose reveal">' + g5p + '</div>\n    </div>\n  </section>\n\n' + cta_band(*cta))

def body_research(lang):
    EL = lang == 'el'
    def ref(cite, note, link, label):
        return ('        <div class="ref reveal"><p class="cite">' + cite + '</p><p class="note">' + note + '</p><a href="' + link + '" target="_blank" rel="noopener noreferrer">' + label + ' →</a></div>\n')
    refs = [
     ('Carrère, J., Reyes, A., Oliveras, L., et al. (2020). <em>The effects of cohousing model on people’s health and wellbeing: a scoping review.</em> Public Health Reviews, 41, 22.',
      'Η σημαντικότερη πηγή για υγεία, ευεξία, κοινωνική υποστήριξη και μοναξιά — θετικές συσχετίσεις, χωρίς όμως απόδειξη αιτίας–αποτελέσματος.' if EL else 'The key source on health, wellbeing, social support and loneliness — positive associations, but without proof of cause and effect.',
      'https://link.springer.com/article/10.1186/s40985-020-00138-1', 'Πλήρης μελέτη — Springer' if EL else 'Full study — Springer'),
     ('Rusinovic, K., van Bochove, M., & van de Sande, J. (2019). <em>Senior Co-Housing in the Netherlands: Benefits and Drawbacks for Its Residents.</em> IJERPH, 16(19), 3776.',
      'Ειδικά για senior co-housing — εξετάζει τα οφέλη αλλά και τις δυσκολίες.' if EL else 'Specifically on senior co-housing — examining both the benefits and the drawbacks.',
      'https://www.mdpi.com/1660-4601/16/19/3776', 'Πλήρης μελέτη — MDPI' if EL else 'Full study — MDPI'),
     ('Wang, J. & Hadjri, K. (2017). <em>The role of co-housing in building sustainable communities: Case studies from the UK.</em> E-BPJ, 2(6), 255–265.',
      'Case studies στο Ηνωμένο Βασίλειο — κοινωνική και περιβαλλοντική βιωσιμότητα.' if EL else 'UK case studies — social and environmental sustainability.',
      'https://eprints.whiterose.ac.uk/id/eprint/142062/', 'Πλήρης μελέτη — White Rose' if EL else 'Full study — White Rose'),
     ('Bianchi, L. & Costa, G. (2024). <em>Living together as a solidarity and generative practice.</em>',
      'Το co-housing ως μορφή συλλογικής κατοίκησης που ενισχύει την αλληλεγγύη και τη δημιουργία κοινοτήτων.' if EL else 'Co-housing as a collective form of living that strengthens solidarity and the creation of communities.',
      'https://www.tandfonline.com/doi/abs/10.1080/03906701.2024.2316509', 'Μελέτη — Taylor & Francis' if EL else 'Study — Taylor & Francis'),
     ('Marckmann, B., Gram-Hanssen, R. & Christensen, T. H. (2012). <em>Sustainable Living and Co-Housing.</em> Built Environment, 38(3).',
      'Σχέση μεταξύ κοινόχρηστων υποδομών, κοινωνικής ζωής και βιώσιμης κατοίκησης.' if EL else 'The relationship between shared infrastructure, social life and sustainable living.',
      'https://www.ingentaconnect.com/content/alex/benv/2012/00000038/00000003/art00007', 'Μελέτη — Ingenta' if EL else 'Study — Ingenta'),
    ]
    if EL:
        H = hero('Συστέγαση / Co-Housing','Έρευνες &<br><em>Τεκμηρίωση.</em>',
            'Τι δείχνουν οι διεθνείς επιστημονικές μελέτες για το Senior Cohousing — με διαφάνεια και σεβασμό στα δεδομένα.',
            '<a href="history.html" class="btn btn-primary">Ιστορία του Cohousing</a> <a href="cohousing.html" class="btn btn-ghost">Το μοντέλο μας</a>',
            'Απεικόνιση','έρευνα / κοινότητα')
        s1e, s1h = 'Τι δείχνουν οι μελέτες', 'Ενθαρρυντικά <em>ευρήματα.</em>'
        s1p = ('<p>Οι έρευνες των τελευταίων ετών δείχνουν ότι το Senior Cohousing μπορεί να προσφέρει σημαντικά οφέλη στην ποιότητα ζωής των ανθρώπων μεγαλύτερης ηλικίας. Η συνύπαρξη ιδιωτικού χώρου με κοινόχρηστους χώρους φαίνεται να ενισχύει την κοινωνική υποστήριξη, την αίσθηση του «ανήκειν» και την ασφάλεια, ενώ μπορούν να περιορίσουν το αίσθημα μοναξιάς.</p>'
               '<p>Το σημαντικότερο: το Co-Housing δεν σημαίνει ότι οι άνθρωποι εγκαταλείπουν την ιδιωτικότητα και την ανεξαρτησία τους. Αντίθετα, βασίζεται στην ισορροπία ανάμεσα στον προσωπικό χώρο και την κοινότητα.</p>')
        note = '<p><strong>Σημείωση διαφάνειας:</strong> Οι επιστημονικές μελέτες είναι ενθαρρυντικές, χωρίς όμως να επιτρέπουν ακόμη να αποδειχθεί ότι το Co-Housing από μόνο του προκαλεί καλύτερη υγεία. Παρουσιάζουμε τα ευρήματα όπως πραγματικά είναι.</p>'
        s2e, s2h = 'Οι επιστημονικές πηγές', 'Πού <em>βασιζόμαστε.</em>'
        cta = ('Μάθε περισσότερα','Δες το δικό μας μοντέλο, ή την ιστορία του Cohousing.',
               '<a href="cohousing.html" class="btn btn-primary">Το μοντέλο μας</a> <a href="history.html" class="btn btn-ghost">Ιστορία του Cohousing</a>')
    else:
        H = hero('Co-Housing','Research &<br><em>Evidence.</em>',
            'What the international scientific studies show about Senior Cohousing — with transparency and respect for the data.',
            '<a href="history.html" class="btn btn-primary">History of Cohousing</a> <a href="cohousing.html" class="btn btn-ghost">Our model</a>',
            'Illustration','research / community')
        s1e, s1h = 'What the studies show', 'Encouraging <em>findings.</em>'
        s1p = ('<p>Research in recent years shows that Senior Cohousing can offer significant benefits to the quality of life of older people. Pairing private space with shared areas appears to strengthen social support, the sense of belonging and safety, while it may reduce feelings of loneliness.</p>'
               '<p>Most importantly: Co-Housing does not mean people give up their privacy and independence. On the contrary, it rests on the balance between personal space and community.</p>')
        note = '<p><strong>A note on transparency:</strong> the scientific studies are encouraging, but they do not yet allow us to prove that Co-Housing on its own causes better health. We present the findings exactly as they are.</p>'
        s2e, s2h = 'The scientific sources', 'What we <em>build on.</em>'
        cta = ('Learn more','See our own model, or the history of Cohousing.',
               '<a href="cohousing.html" class="btn btn-primary">Our model</a> <a href="history.html" class="btn btn-ghost">History of Cohousing</a>')
    refs_html = "".join(ref(c, n, l, lb) for c, n, l, lb in refs)
    return (H +
     '  <section class="section">\n    <div class="wrap">\n' + sechead(s1e, s1h) +
     '      <div class="prose reveal">' + s1p + '</div>\n'
     '      <div class="callout reveal">' + note + '</div>\n    </div>\n  </section>\n\n'
     '  <section class="section warm">\n    <div class="wrap">\n' + sechead(s2e, s2h) +
     '      <div class="ref-list">\n' + refs_html + '      </div>\n    </div>\n  </section>\n\n' + cta_band(*cta))

# ============================================================ PAGE REGISTRY
PAGES = [
 ('index.html','home','', body_home,
  {'el':('ΕΣΤΙΑ — Ζούμε Μαζί · Συνεργατική Διαβίωση 60+ στην Αθήνα','Η ΕΣΤΙΑ φέρνει το μοντέλο senior cohousing στην Αθήνα: αυτόνομη συστέγαση για ανθρώπους 60+, με ιδιωτικό χώρο και μια δεμένη κοινότητα.'),
   'en':('ESTIA — Living Together · Senior Co-Living 60+ in Athens','ESTIA brings the senior cohousing model to Athens: independent co-living for people 60+, with private space and a close-knit community.')}),
 ('cohousing.html','cohousing','model', body_cohousing,
  {'el':('Το μοντέλο μας — ΕΣΤΙΑ · Συστέγαση / Co-Housing','Πώς λειτουργεί το μοντέλο της ΕΣΤΙΑ: ιδιωτικός χώρος 21 τ.μ. ανά άτομο με δικό σου μπάνιο και γραφείο, κοινόχρηστοι χώροι, κήπος και περισσότερα.'),
   'en':('Our Model — ESTIA · Co-Housing','How the ESTIA model works: 21 m² of private space per person with your own bathroom and study, shared areas, a garden and more.')}),
 ('technology.html','cohousing','technology', body_technology,
  {'el':('Τεχνολογία — ΕΣΤΙΑ','Η τεχνολογία της ΕΣΤΙΑ: έξυπνο σπίτι, βιωσιμότητα, λογισμικό ταιριάσματος ανθρώπων και αναφοράς.'),
   'en':('Technology — ESTIA','The technology of ESTIA: smart home, sustainability, people-matching software and a reporting platform.')}),
 ('membership.html','membership','', body_membership,
  {'el':('Γίνε Μέλος — ΕΣΤΙΑ','Τα βήματα για να γίνεις μέλος της κοινότητας ΕΣΤΙΑ, και η δυνατότητα αξιοποίησης του προηγούμενου σπιτιού σου.'),
   'en':('Become a Member — ESTIA','The steps to join the ESTIA community, and the option to make your previous home work for you.')}),
 ('municipalities.html','municipalities','', body_municipalities,
  {'el':('Για Δήμους — ΕΣΤΙΑ','Συνεργασία με δήμους: διαθέτετε ακίνητο, εμείς το ανακαινίζουμε, και εξασφαλίζετε θέσεις για δικούς σας κατοίκους.'),
   'en':('For Municipalities — ESTIA','Partnership with municipalities: you provide a building, we renovate it, and you secure places for your own residents.')}),
 ('expats.html','expats','', body_expats,
  {'el':('Για Ξένους — ΕΣΤΙΑ','Συνταξιοδότηση στην Ελλάδα με την ΕΣΤΙΑ: έτοιμη κοινότητα και πλήρεις υπηρεσίες μετακόμισης — από την απόφαση μέχρι το κλειδί.'),
   'en':('For Expats — ESTIA','Retire in Greece with ESTIA: a ready-made community and full relocation services — from your decision to the key.')}),
 ('about.html','about','aboutus', body_about,
  {'el':('Ποιοι Είμαστε — ΕΣΤΙΑ','Η ιστορία, οι αξίες και η ομάδα πίσω από την ΕΣΤΙΑ.'),
   'en':('About Us — ESTIA','The story, the values and the team behind ESTIA.')}),
 ('careers.html','about','careers', body_careers,
  {'el':('Καριέρα — ΕΣΤΙΑ','Ανοιχτές θέσεις εργασίας στην ΕΣΤΙΑ. Έλα να χτίσουμε μαζί το μέλλον της συνεργατικής διαβίωσης στην Ελλάδα.'),
   'en':('Careers — ESTIA','Open roles at ESTIA. Come build the future of co-living in Greece with us.')}),
 ('news.html','updates','news', body_news,
  {'el':('Νέα — ΕΣΤΙΑ','Τα νέα και οι ανακοινώσεις της ΕΣΤΙΑ.'),
   'en':('News — ESTIA','News and announcements from ESTIA.')}),
 ('blog.html','updates','blog', body_blog,
  {'el':('Blog — ΕΣΤΙΑ','Άρθρα και συμβουλές για τη ζωή σε κοινότητα και την τρίτη ηλικία.'),
   'en':('Blog — ESTIA','Articles and advice on community living and later life.')}),
 ('contact.html','contact','', body_contact,
  {'el':('Επικοινωνία — ΕΣΤΙΑ','Επικοινώνησε με την ΕΣΤΙΑ — συμπλήρωσε τη φόρμα και θα σε καλέσουμε.'),
   'en':('Contact — ESTIA','Get in touch with ESTIA — fill in the form and we will call you.')}),
 ('history.html','cohousing','history', body_history,
  {'el':('Ιστορία του Cohousing — ΕΣΤΙΑ','Η ιστορία του Cohousing — από τη Δανία του 1972 μέχρι τις σύγχρονες κοινότητες.'),
   'en':('History of Cohousing — ESTIA','The history of Cohousing — from 1972 Denmark to modern communities.')}),
 ('research.html','cohousing','research', body_research,
  {'el':('Έρευνες & Τεκμηρίωση — ΕΣΤΙΑ','Τι δείχνουν οι διεθνείς επιστημονικές μελέτες για το Senior Cohousing, με τις πηγές.'),
   'en':('Research & Evidence — ESTIA','What the international scientific studies show about Senior Cohousing, with the sources.')}),
]

# ============================================================ BUILD
def build():
    for lang in ('el', 'en'):
        p = '' if lang == 'el' else '../'
        outdir = ROOT if lang == 'el' else os.path.join(ROOT, 'en')
        os.makedirs(outdir, exist_ok=True)
        for name, active, sub, builder, meta in PAGES:
            CURRENT[0] = name
            title, desc = meta[lang]
            html = head(lang, p, title, desc) + nav(lang, p, active, sub) + builder(lang) + footer(lang, p)
            with open(os.path.join(outdir, name), 'w', encoding='utf-8') as f:
                f.write(html)
            print('wrote', lang, name, len(html))
    print('DONE')

if __name__ == '__main__':
    build()
