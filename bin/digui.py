import requests
from conf.config import *

def init_url(url, data):
    page = requests.post(url=url, data=data, headers=headers)
    page_jsons = page.json()
    for page_json in page_jsons:
        print(page_json['name'])