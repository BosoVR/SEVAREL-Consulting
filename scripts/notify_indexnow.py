"""Notify IndexNow only after the exact approved sitemap and key file are live."""
import argparse, json, re, time, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://sevarel-consulting.de'

def request(url, data=None):
    req = urllib.request.Request(url, data=data, headers={'User-Agent':'SEVAREL-IndexNow/1.0', 'Content-Type':'application/json; charset=utf-8'} if data else {'User-Agent':'SEVAREL-IndexNow/1.0'})
    with urllib.request.urlopen(req, timeout=20) as response:
        return response.status, response.read()

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--wait-seconds',type=int,default=0); parser.add_argument('--dry-run',action='store_true'); args=parser.parse_args()
    manifest=json.loads((ROOT/'deploy-manifest.json').read_text(encoding='utf-8'))
    keyfile=manifest['indexnow_key_file']
    if not re.fullmatch(r'[a-f0-9]{32}\.txt',keyfile): raise ValueError('Invalid IndexNow proof filename')
    key=keyfile[:-4]
    sitemap=(ROOT/'website/sitemap.xml').read_bytes()
    expected=[n.text for n in ET.fromstring(sitemap).findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    if not expected or len(expected)!=len(set(expected)) or any(not u.startswith(ORIGIN+'/') for u in expected): raise ValueError('Unsafe sitemap')
    deadline=time.monotonic()+args.wait_seconds
    while True:
        try:
            _,live=request(ORIGIN+'/sitemap.xml')
            _,proof=request(ORIGIN+'/'+keyfile)
            _,info=request(ORIGIN+'/build-info.json')
            if live!=sitemap or proof.decode().strip()!=key or json.loads(info)['version']!=manifest['version']: raise ValueError('Approved publication is not live yet')
            break
        except (OSError,ValueError):
            if time.monotonic()>=deadline: raise
            time.sleep(10)
    payload={'host':'sevarel-consulting.de','key':key,'keyLocation':ORIGIN+'/'+keyfile,'urlList':expected}
    if args.dry_run:
        print(json.dumps({'dry_run':True,'validated_urls':len(expected),'publication_version':manifest['version']})); return
    status,_=request('https://api.indexnow.org/indexnow',json.dumps(payload).encode())
    if status not in (200,202):raise ValueError('IndexNow did not accept URLs')
    print(json.dumps({'submitted_urls':len(expected),'http_status':status,'key_validation_pending':status==202,'publication_version':manifest['version']}))

if __name__=='__main__':main()
