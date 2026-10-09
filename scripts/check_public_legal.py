"""Check publication-critical notices in the actual extracted hosting artifact."""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1] / 'website'
pages = list(root.rglob('*.html'))
assert len(pages) == 59
for page in pages:
    html = page.read_text(encoding='utf-8')
    assert not any(marker in html for marker in ('Ã¤','Ã¼','Ã¶','Ãœ','ÃŸ')), f'Damaged German UTF-8 text: {page}'
    assert 'KI-generierte Illustrationen' in html, page
    assert 'ausschließlich an Unternehmen' in html, page
    assert 'Anbieter- und Veröffentlichungsfreigabe stehen aus' not in html, page
privacy = (root/'datenschutz/index.html').read_text(encoding='utf-8')
assert 'Cloudflare, Inc.' in privacy and 'DeinServerHost' in privacy
assert 'Beim späteren Online-Abruf' not in privacy
for name in ('impressum','datenschutz'):
    html = (root/name/'index.html').read_text(encoding='utf-8')
    start = html.index('<!--email_off-->')
    end = html.index('<!--/email_off-->', start)
    assert 'mailto:info@sevarel-consulting.de' in html[start:end], name
editorial = (root/'redaktion/index.html').read_text(encoding='utf-8')
assert 'Marvin Malessa persönlich inhaltlich geprüft' in editorial
usage = (root/'downloads/nutzungshinweise.md').read_bytes()
for archive in (root/'downloads').glob('*.zip'):
    with zipfile.ZipFile(archive) as bundle:
        assert bundle.read('NUTZUNGSHINWEISE.md') == usage, archive
print('59 öffentliche Seiten und alle vier Download-Pakete: Veröffentlichungshinweise geprüft.')
