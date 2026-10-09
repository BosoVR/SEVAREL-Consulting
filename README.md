# SEVAREL Consulting

Cloudflare-Pages-Import für die korrigierte Website-Version **4.4.9**.
Die Version ergänzt Datenschutzinformationen, Geschäftskunden-Hinweise, sichtbare
KI-Bildkennzeichnung, die bestätigte persönliche Inhaltsprüfung und Nutzungsbedingungen
für Vorlagen und Download-Pakete. Eine anwaltliche Freigabe wird nicht behauptet.
Die redaktionellen Abschnitte verwenden ein gemeinsames Spaltenraster und bündige
Textkanten. Der Werkzeugabschnitt bleibt innerhalb derselben Inhaltsbreite.
Schriften sind weiterhin Systemschriften; fremde Marken-Schriftdateien wurden nicht importiert.
Alle 17 Wissensartikel enthalten eingeordnete Primärquellen und einen sichtbaren
Hinweis auf die bestätigte persönliche Inhaltsprüfung. Das Organisationsschema
enthält die tatsächliche Telefonnummer und eine strukturierte Geschäftsanschrift.
Die Google-SEO-Überarbeitung präzisiert die Suchtexte von neun Seiten, behebt den
doppelten Einstieg des Prozesskennzahlen-Artikels und ergänzt Aufgabenbezug,
Anbieteridentität sowie relevante interne Leitfadenlinks. Sitemap und strukturierte
Daten enthalten die tatsächlichen Änderungsstände; die Indexierung bleibt freigegeben.

## Bereitstellung

Das geprüfte Hosting-Paket ist im Repository enthalten:

`SEVAREL-Consulting-Hosting-v4-4-9.zip`

Die GitHub-Anbindung an Cloudflare Pages ist eingerichtet. Der Push auf `main`
wurde erfolgreich gebaut und veröffentlicht. GitHub Actions prüft zusätzlich
die Archivintegrität und alle 59 HTML-Seiten.

- Website: https://sevarel-consulting.de
- www: https://www.sevarel-consulting.de
- Cloudflare-Adresse: https://sevarel-consulting.pages.dev

Die Domain bleibt bei Deinserverhost registriert. Die Nameserver sind auf
`eva.ns.cloudflare.com` und `lennox.ns.cloudflare.com` umgestellt.
Beide eigenen Domains sind in Cloudflare aktiv; gültige HTTPS-Zertifikate und
HTTP 200 wurden direkt gegen autoritative Cloudflare-IP-Adressen geprüft.
DNS-Zwischenspeicher können während der Umstellung noch alte Antworten liefern.

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
**235 geprüfte öffentliche Dateien, darunter 59 HTML-Seiten**, nach `website/`.
Cloudflare veröffentlicht nur diesen Ausgabeordner, nicht diese README oder das Archiv.
Header-Regeln und Weiterleitungen aus dem Hosting-Paket bleiben erhalten.

## Betriebsstand

- Die Indexierung ist ausdrücklich freigegeben: 54 Inhaltsseiten stehen in der Sitemap.
- Kanonische URLs verweisen auf `https://sevarel-consulting.de`; Rechtsseiten und 404 bleiben `noindex`.
- Das Kontaktformular erzeugt einen lokalen Anfragebrief. Es versendet keine E-Mail.
- Die vorhandenen direkten Telefon-/E-Mail-Links bleiben bestehen.
- Das Impressum enthält die bestätigten Anbieterangaben; eine Wirtschafts-ID ist noch nicht zugeteilt.
- Cloudflare Bot Fight Mode und dessen automatische JavaScript-Erkennung wurden
  nach ausdrücklicher Zustimmung deaktiviert; die Datenschutzseite beschreibt dies.
- Der Nachweis eines Auftragsverarbeitungsvertrags für das DeinServerHost-Postfach
  steht noch aus.
- Interne Unterlagen, Kunden-Arbeitspaket und Entwicklungsdokumente sind nicht Teil dieses Imports.

Cloudflare Pages ist mit `BosoVR/SEVAREL-Consulting` verbunden und veröffentlicht
Änderungen auf `main` automatisch. Der vollständige Entwicklungs- und
Dokumentbestand liegt im lokalen Arbeitsordner; dieses öffentliche Repository
enthält den geprüften Hosting-Import.

## Lokal prüfen

Bing Webmaster Tools ist per DNS verifiziert. Die Sitemap wurde eingereicht.
Der IndexNow-Workflow meldet nach erfolgreicher Live-Prüfung die 54 Sitemap-URLs
an den IndexNow-Verbund. Er wartet auf die passende veröffentlichte Version,
prüft den öffentlich ausgelieferten Besitznachweis und übermittelt ausschließlich
URLs der eigenen Domain. Eine Annahme der Meldung garantiert keine Indexierung.

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
