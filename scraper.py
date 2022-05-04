# TODO: finish this later, when it's needed

import requests
from bs4 import BeautifulSoup

def get_webpage():
    r = requests.get(
        'https://www.wowhead.com/item=173058/umbral-ink',
        stream=True
    )

    with open("webpage.html", 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
