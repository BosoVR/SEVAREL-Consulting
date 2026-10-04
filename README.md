# SEVAREL Consulting

Cloudflare-Pages-Import für die zuletzt korrigierte Website-Version **4.4.1**.
Design, Logo, Texte, Animationen und Dokumente werden durch diesen Import nicht verändert.

## Einmalig: Hosting-Datei hinzufügen

Die Website-ZIP muss zusätzlich zu diesen Konfigurationsdateien im Repository liegen:

`SEVAREL-Consulting-Hosting-v4-4-1.zip`

Auf GitHub **Add file > Upload files** wählen, genau diese Hosting-ZIP in das
Hauptverzeichnis ziehen und auf `main` committen. **Nicht entpacken, nicht umbenennen.**
Nicht das Komplettpaket oder die große Offline-Vorschau hochladen.
Der Build bricht mit einer klaren Meldung ab, solange die richtige ZIP fehlt.

## Cloudflare Pages

In Cloudflare ein **Pages-Projekt** erstellen, GitHub verbinden und dieses Repository auswählen.

| Einstellung | Wert |
| --- | --- |
| Repository | `BosoVR/SEVAREL-Consulting` |
| Produktionsbranch | `main` |
| Framework | `None` / kein Framework |
| Root directory | leer lassen (Repository-Hauptverzeichnis) |
| Build command | `python3 scripts/prepare_cloudflare.py` |
| Build output directory | `website` |

Python 3 ist in der aktuellen Cloudflare-Pages-Buildumgebung vorhanden.
Der Import benötigt keine zusätzlichen Pakete, API-Schlüssel oder externen Downloads.
`wrangler.toml` legt den Ausgabeordner ebenfalls fest. Keinen Worker-Deploy-Befehl eintragen.

Der Build prüft die SHA-256-Prüfsumme der ZIP, entpackt sie sicher und liefert
**233 unveränderte öffentliche Dateien, darunter 59 HTML-Seiten**, nach `website/`.
Cloudflare veröffentlicht nur diesen Ausgabeordner, nicht diese README oder das Archiv.
Header-Regeln und Weiterleitungen aus dem Hosting-Paket bleiben erhalten.

## Bewusst erhaltener Vorschauzustand

- `noindex` bleibt gesetzt; dies ist kein Passwortschutz.
- Das Kontaktformular erzeugt einen lokalen Anfragebrief. Es versendet keine E-Mail.
- Die vorhandenen direkten Telefon-/E-Mail-Links bleiben bestehen.
- Keine neue Domain, Mailbox, Datenschutzfreigabe oder rechtliche Freigabe wird angenommen.
- Interne Unterlagen, Kunden-Arbeitspaket und Entwicklungsdokumente sind nicht Teil dieses Imports.

Die Verbindung zu Cloudflare muss im eigenen Cloudflare-Konto hergestellt werden.
Ein GitHub-Commit allein bestätigt noch keinen erfolgreichen Cloudflare-Deploy.

## Lokal prüfen

```sh
python3 scripts/prepare_cloudflare.py
python3 -m http.server 8080 --directory website
```

Neue Website-Versionen benötigen ein neues geprüftes Hosting-Paket und die passende
Prüfsumme sowie Dateizählung in `deploy-manifest.json`. Die Ausgabe `website/`
wird nur dann ersetzt, wenn sie vorher von diesem Skript erzeugt wurde.

## Offizielle Dokumentation

- [Cloudflare Pages: Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/)
- [Cloudflare Pages: Build configuration](https://developers.cloudflare.com/pages/configuration/build-configuration/)
- [Cloudflare Pages: Build image](https://developers.cloudflare.com/pages/configuration/build-image/)
