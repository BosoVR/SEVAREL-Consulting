import json, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import notify_indexnow as notifier

class IndexNowPublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        (self.root/'website').mkdir();self.key='a'*32
        self.manifest={'version':'test','indexnow_key_file':self.key+'.txt'}
        (self.root/'deploy-manifest.json').write_text(json.dumps(self.manifest))
        self.sitemap=b'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://sevarel-consulting.de/</loc></url></urlset>'
        (self.root/'website/sitemap.xml').write_bytes(self.sitemap)
        self.posts=[]
    def tearDown(self):self.temp.cleanup()
    def response(self,url,data=None):
        if data:self.posts.append(json.loads(data));return 200,b''
        if url.endswith('sitemap.xml'):return 200,self.sitemap
        if url.endswith('build-info.json'):return 200,b'{"version":"test"}'
        return 200,self.key.encode()
    def execute(self,handler=None):
        with patch.object(notifier,'ROOT',self.root),patch.object(notifier,'request',handler or self.response),patch('sys.argv',['notify_indexnow.py']):notifier.main()
    def test_verified_publication_posts_only_own_sitemap_urls(self):
        self.execute();self.assertEqual(len(self.posts),1)
        self.assertEqual(self.posts[0]['urlList'],['https://sevarel-consulting.de/'])
    def test_unpublished_key_never_submits(self):
        def wrong_key(url,data=None):
            if url.endswith('.txt'):return 200,b'wrong-key'
            return self.response(url,data)
        with self.assertRaises(ValueError):self.execute(wrong_key)
        self.assertEqual(self.posts,[])
    def test_foreign_host_never_reaches_network(self):
        (self.root/'website/sitemap.xml').write_bytes(self.sitemap.replace(b'sevarel-consulting.de',b'other.example'))
        with self.assertRaises(ValueError),patch.object(notifier,'request') as network:
            self.execute(network)
        network.assert_not_called()
    def test_stale_deployment_never_submits(self):
        def stale(url,data=None):
            if url.endswith('build-info.json'):return 200,b'{"version":"old"}'
            return self.response(url,data)
        with self.assertRaises(ValueError):self.execute(stale)
        self.assertEqual(self.posts,[])

if __name__=='__main__':unittest.main()
