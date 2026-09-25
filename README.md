# Mathe-Jeopardy

Quiz-Tafel im Stil von Jeopardy für den Unterricht am Beamer – bis 6 Gruppen, Countdown mit Signaltönen, «Erben» bei falschen Antworten, Rückmeldung pro Gruppe.

## Spielen

- **Online:** Die Datei `index.html` im Browser öffnen (oder den GitHub-Pages-Link).
- Spiele, Runden und Klassenlisten werden **nur im eigenen Browser** gespeichert.
- Spiele lassen sich als Datei herunterladen und mit «Spiel-Datei laden» weitergeben.
- Neue Spiele: selbst erfassen oder «Mit KI erstellen» (Auftrag in Copilot, ChatGPT oder Claude einfügen).

Bitte bei Klassenlisten nur Vornamen oder Kürzel verwenden.

## Sammlung

Im Ordner `spiele/` liegen Spiele zum Übernehmen. Auf der Seite erscheinen sie unter «Aus der Sammlung»
(nur über den GitHub-Pages-Link, nicht beim direkten Öffnen der Datei).

- **Eigene Spiele teilen:** In der claude.ai-Version beim Spiel «In der öffentlichen Sammlung teilen» ankreuzen,
  dann Claude sagen: «Aktualisiere die Sammlung». Danach in GitHub Desktop «Push origin».
- **Spiele von anderen:** Heruntergeladene Spiel-Datei (`.json`) in `spiele/` legen und `python3 sammlung.py` ausführen.
- Wer ein Spiel übernommen hat, besitzt eine eigene Kopie. Gibt es eine neuere Fassung, zeigt die Seite das an.
- Die Sammlung ist öffentlich: keine Schülerdaten und keine wörtlich abgeschriebenen Lehrmittel-Aufgaben.

## Dateien

| Datei | Zweck |
|---|---|
| `claude-artifact.html` | Quelle – wird auch auf claude.ai veröffentlicht |
| `index.html` | Eigenständige Version für Browser und GitHub Pages (wird mit `build.sh` erzeugt) |
| `build.sh` | Erstellt `index.html` aus `claude-artifact.html` |
| `spiele/` | Öffentliche Spielsammlung, `index.json` ist das Verzeichnis |
| `sammlung.py` | Aktualisiert `spiele/` und `spiele/index.json` |
