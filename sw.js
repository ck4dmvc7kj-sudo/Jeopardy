/* Offline-Start für die App auf dem Home-Bildschirm.
   - Programm und Sammlung: zuerst aus dem Netz (immer die neueste Fassung), ohne Netz aus dem Speicher.
   - Schriften von Google: einmal laden, danach aus dem Speicher.
   Bei grösseren Änderungen an dieser Datei die Versionsnummer erhöhen. */
const CACHE = 'jeopardy-v1';
const CORE = ['./', './index.html', './manifest.webmanifest', './icons/icon-180.png', './icons/icon-192.png', './icons/icon-512.png'];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

function remember(req, res){
  if (res && (res.ok || res.type === 'opaque')){
    const copy = res.clone();
    caches.open(CACHE).then(c => c.put(req, copy));
  }
  return res;
}

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  if (url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com'){
    event.respondWith(caches.match(req).then(hit => hit || fetch(req).then(res => remember(req, res))));
    return;
  }
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    fetch(req)
      .then(res => remember(req, res))
      .catch(() => caches.match(req, { ignoreSearch: true })
        .then(hit => hit || (req.mode === 'navigate' ? caches.match('./index.html') : null))
        .then(hit => hit || Response.error()))
  );
});
