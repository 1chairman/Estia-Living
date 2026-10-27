/* ΕΣΤΙΑ — service worker.
   Η εφαρμογή πρέπει να ανοίγει χωρίς δίκτυο: ένας ηλικιωμένος στο υπόγειο με
   χαλασμένο ασανσέρ δεν έχει σήμα. Ό,τι χρειάζεται για να φορτώσει η οθόνη
   μπαίνει στην cache κατά την εγκατάσταση. */
const V = 'estia-v1';
const CORE = ['./', './index.html', './manifest.webmanifest',
              './icons/icon-192.png', './icons/icon-512.png',
              './icons/apple-touch-icon.png', './icons/icon-maskable-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(V).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(ks => Promise.all(ks.filter(k => k !== V).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  /* Δίκτυο πρώτα για το HTML, ώστε μια νέα έκδοση να φτάνει αμέσως· cache ως
     δίχτυ ασφαλείας. Στατικά αρχεία: cache πρώτα, γιατί δεν αλλάζουν. */
  const isDoc = e.request.mode === 'navigate';
  if (isDoc) {
    e.respondWith(fetch(e.request)
      .then(r => { const cp = r.clone(); caches.open(V).then(c => c.put(e.request, cp)); return r })
      .catch(() => caches.match(e.request).then(r => r || caches.match('./index.html'))));
  } else {
    e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)
      .then(res => { const cp = res.clone();
        caches.open(V).then(c => c.put(e.request, cp)); return res })
      .catch(() => r)));
  }
});
