#!/bin/sh
# Erstellt index.html (eigenständige Version für Browser, Kollegium und GitHub Pages)
# aus claude-artifact.html (Quelle, die auch auf claude.ai veröffentlicht wird).
# Dazu kommen die Angaben für die App auf dem Home-Bildschirm (iPad) und der Offline-Start (sw.js).
cd "$(dirname "$0")"
{
  printf '%s\n' '<!doctype html>' '<html lang="de-CH">' '<head>' '<meta charset="utf-8">' \
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">' \
    '<link rel="manifest" href="manifest.webmanifest">' \
    '<link rel="apple-touch-icon" href="icons/icon-180.png">' \
    '<meta name="apple-mobile-web-app-capable" content="yes">' \
    '<meta name="mobile-web-app-capable" content="yes">' \
    '<meta name="apple-mobile-web-app-status-bar-style" content="black">' \
    '<meta name="apple-mobile-web-app-title" content="Jeopardy">' \
    '<meta name="theme-color" content="#18221f">' \
    '<style>[hidden]{display:none!important}img{max-width:100%}</style>' \
    "<script>if ('serviceWorker' in navigator && (location.protocol === 'https:' || /^(localhost|127\\.0\\.0\\.1)$/.test(location.hostname))) addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));</script>"
  cat claude-artifact.html
  printf '%s\n' '</html>'
} > index.html
echo "index.html aktualisiert"
