import requests
from requests_oauthlib import OAuth1
import os
from urllib.parse import urljoin
from dotenv import load_dotenv

load_dotenv()


class IconGetter:
    def __init__(self):
        self._auth = OAuth1(os.getenv('KEY'), os.getenv('SECRET'))
        self._endpoint = "http://api.thenounproject.com/icon/"
        self.icon = None

    def get_icon(self, id):
        url = urljoin(self._endpoint, str(id))
        response = requests.get(url, auth=self._auth)
        result = response.json()
        icon_url = result['icon']['icon_url']
        # self.icon = requests.get(icon_url).content
        self.icon = self._get_icon(icon_url)

    def _get_icon(self, icon_url):
        response = requests.get(icon_url)
        return response.content

    def write_icon(self, filename):
        with open(filename, 'wb') as file:
            file.write(self.icon)


icon_getter = IconGetter()
icon_getter.get_icon("1")
print(icon_getter.icon)
icon_getter.write_icon("alphabet/test.svg")
