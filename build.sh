#!/bin/sh
# Erstellt index.html (eigenständige Version für Browser, Kollegium und GitHub Pages)
# aus claude-artifact.html (Quelle, die auch auf claude.ai veröffentlicht wird).
cd "$(dirname "$0")"
{
  printf '%s\n' '<!doctype html>' '<html lang="de-CH">' '<head>' '<meta charset="utf-8">' \
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">' \
    '<style>[hidden]{display:none!important}img{max-width:100%}</style>'
  cat claude-artifact.html
  printf '%s\n' '</html>'
} > index.html
echo "index.html aktualisiert"
