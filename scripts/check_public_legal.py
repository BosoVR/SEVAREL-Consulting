"""Check publication-critical notices in the actual extracted hosting artifact."""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1] / 'website'
pages = list(root.rglob('*.html'))
assert len(pages) == 59
for page in pages:
    html = page.read_text(encoding='utf-8')
    assert 'KI-generierte Illustrationen' in html, page
    assert 'ausschlieÃŸlich an Unternehmen' in html, page
    assert 'Anbieter- und VerÃ¶ffentlichungsfreigabe stehen aus' not in html, page
privacy = (root/'datenschutz/index.html').read_text(encoding='utf-8')
assert 'Cloudflare, Inc.' in privacy and 'DeinServerHost' in privacy
assert 'Beim spÃ¤teren Online-Abruf' not in privacy
for name in ('impressum','datenschutz'):
    html = (root/name/'index.html').read_text(encoding='utf-8')
    start = html.index('<!--email_off-->')
    end = html.index('<!--/email_off-->', start)
    assert 'mailto:info@sevarel-consulting.de' in html[start:end], name
editorial = (root/'redaktion/index.html').read_text(encoding='utf-8')
assert 'Marvin Malessa persÃ¶nlich inhaltlich geprÃ¼ft' in editorial
usage = (root/'downloads/nutzungshinweise.md').read_bytes()
for archive in (root/'downloads').glob('*.zip'):
    with zipfile.ZipFile(archive) as bundle:
        assert bundle.read('NUTZUNGSHINWEISE.md') == usage, archive
print('59 Ã¶ffentliche Seiten und alle vier Download-Pakete: VerÃ¶ffentlichungshinweise geprÃ¼ft.')
