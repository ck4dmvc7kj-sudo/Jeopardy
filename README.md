# Mathe-Jeopardy

Quiz-Tafel im Stil von Jeopardy für den Unterricht am Beamer – bis 6 Gruppen, Countdown mit Signaltönen, «Erben» bei falschen Antworten, Rückmeldung pro Gruppe.

## Spielen

- **Online:** Die Datei `index.html` im Browser öffnen (oder den GitHub-Pages-Link).
- Spiele, Runden und Klassenlisten werden **nur im eigenen Browser** gespeichert.
- Spiele lassen sich als Datei herunterladen und mit «Spiel-Datei laden» weitergeben.
- Neue Spiele: selbst erfassen oder «Mit KI erstellen» (Auftrag in Copilot, ChatGPT oder Claude einfügen).

Bitte bei Klassenlisten nur Vornamen oder Kürzel verwenden.

## Dateien

| Datei | Zweck |
|---|---|
| `claude-artifact.html` | Quelle – wird auch auf claude.ai veröffentlicht |
| `index.html` | Eigenständige Version für Browser und GitHub Pages (wird mit `build.sh` erzeugt) |
| `build.sh` | Erstellt `index.html` aus `claude-artifact.html` |
