/* Hosted companion only: the game itself is self-contained in index.html. */
'use strict';
const CACHE = 'reading-garden-shell-v1';
const ROOT = self.registration.scope;
const SHELL = ['index.html', './', 'manifest.webmanifest', 'icons/icon-192.png', 'icons/icon-512.png', 'icons/apple-touch-icon.png'].map(p => new URL(p, ROOT).href);
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(SHELL)));
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(names => Promise.all(names.filter(name => name.startsWith('reading-garden-shell-') && name !== CACHE).map(name => caches.delete(name)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', event => {
  const req = event.request;
  const url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== self.location.origin || !req.url.startsWith(ROOT)) return;
  if (req.mode === 'navigate') {
    event.respondWith(fetch(req).catch(async () => (await caches.open(CACHE)).match(new URL('index.html', ROOT).href)));
  } else if (SHELL.includes(url.href)) {
    event.respondWith(caches.open(CACHE).then(async cache => (await cache.match(req)) || fetch(req)));
  }
});
