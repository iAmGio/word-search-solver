import json
import urllib3
import certifi
from bs4 import BeautifulSoup


class WebParser:

    def __init__(self, url):
        self.url = url

    def parse(self):
        page = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
        ).request('GET', self.url).data
        return BeautifulSoup(page, features="html.parser").prettify()

    def parse_to_array(self):
        return json.loads(self.parse())
