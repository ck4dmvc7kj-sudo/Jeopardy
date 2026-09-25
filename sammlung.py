#!/usr/bin/env python3
"""Pflegt die öffentliche Spielsammlung im Ordner spiele/.

Aufruf:
  python3 sammlung.py                 # nur spiele/index.json neu erstellen
  python3 sammlung.py <db-export>     # zusätzlich Spiele aus einem Export der claude.ai-Datenbank übernehmen

<db-export> ist ein Ordner mit JSON-Dateien der Sammlung «sets» (ein Spiel pro Datei).
Übernommen werden nur Spiele mit «In der öffentlichen Sammlung teilen» (shared = true);
Spiele, bei denen das Häkchen entfernt wurde, werden aus spiele/ gelöscht.
Von Hand in spiele/ abgelegte Spiel-Dateien (z. B. von Kolleginnen und Kollegen) bleiben erhalten.
"""
import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SPIELE = ROOT / "spiele"
PRIVATE = ("id", "updatedAt", "createdBy", "shared", "fromCollection", "collectionStand")


def stand_from_ms(ms):
    return datetime.datetime.fromtimestamp(ms / 1000).strftime("%Y-%m-%dT%H:%M")


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue"))
    return s.strip("-")[:50] or "spiel"


def sync_from_db(export_dir):
    """Geteilte Spiele aus dem Datenbank-Export nach spiele/ schreiben."""
    SPIELE.mkdir(exist_ok=True)
    for f in sorted(pathlib.Path(export_dir).rglob("*.json")):
        doc = json.loads(f.read_text(encoding="utf-8"))
        data = doc.get("data", doc)
        set_id = doc.get("id") or data.get("id") or f.stem
        target = SPIELE / f"{set_id}.json"
        if not data.get("shared"):
            if target.exists():
                target.unlink()
                print("entfernt:", data.get("title"))
            continue
        game = {"format": "mathe-jeopardy", "version": 1}
        game.update({k: v for k, v in data.items() if k not in PRIVATE})
        game["sammlung"] = {"id": set_id, "stand": stand_from_ms(data.get("updatedAt") or 0)}
        text = json.dumps(game, ensure_ascii=False, indent=2) + "\n"
        if not target.exists() or target.read_text(encoding="utf-8") != text:
            target.write_text(text, encoding="utf-8")
            print("aktualisiert:", game.get("title"))


def build_index():
    """spiele/index.json aus allen Spiel-Dateien erstellen."""
    SPIELE.mkdir(exist_ok=True)
    items = []
    for f in sorted(SPIELE.glob("*.json")):
        if f.name == "index.json":
            continue
        g = json.loads(f.read_text(encoding="utf-8"))
        meta = g.get("sammlung") or {}
        cols, rows = int(g.get("cols", 5)), int(g.get("rows", 10))
        items.append({
            "id": meta.get("id") or "datei-" + slug(f.stem),
            "file": f.name,
            "title": g.get("title") or f.stem,
            "cols": cols,
            "rows": rows,
            "topics": [c.get("name", "") for c in (g.get("categories") or [])[:cols]],
            "stand": meta.get("stand") or stand_from_ms(f.stat().st_mtime * 1000),
        })
    items.sort(key=lambda x: x["title"].lower())
    (SPIELE / "index.json").write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"index.json: {len(items)} Spiele")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        sync_from_db(sys.argv[1])
    build_index()
