import requests
from conf.config import *
import json
from bin.connect import collection
import time

def init_url(data):
    while True:
        try:
            headers['User-Agent'] = User_Agent[random.randint(0,len(User_Agent)-1)]
            page = requests.post(url=url, data=data, headers=headers)
            page_jsons = page.json()
            break
        except:
            pass
    for page_json in page_jsons:
        if page_json['isParent']:
            page_data = {
                'id': page_json['id'],
                'dbcode': 'hgnd',
                'wdcode': 'zb',
                'm': 'getTree'
            }
            init_url(data=page_data)
        else:
            kw = {
                'm': 'QueryData',
                'dbcode': 'hgnd',
                'rowcode': 'zb',
                'colcode': 'sj',
                'wds': json.dumps([]),
                'dfwds': json.dumps([{"wdcode": "zb", "valuecode": page_json['id']}])
            }
            while True:
                try:
                    headers['User-Agent'] = User_Agent[random.randint(0, len(User_Agent) - 1)]
                    page_data_k = requests.get(url=data_url,params=kw,headers=headers)
                    page_data_json = page_data_k.json()
                    break
                except:
                    pass
            num_to_string = {}
            for page_data_ye in page_data_json['returndata']['wdnodes']:
                if page_data_ye['wdcode']=='zb':
                    for ye in page_data_ye['nodes']:
                        num_to_string[ye['code']] = ye['cname']
            for page_data_ye in page_data_json['returndata']['datanodes']:
                shuju = page_data_ye['data']['data']
                year = None
                title = None
                for ye in page_data_ye['wds']:
                    if ye['wdcode']=='zb':
                        title = num_to_string[ye['valuecode']]
                    if ye['wdcode']=='sj':
                        year = ye['valuecode']
                info = {
                    'title':title,
                    'year':year,
                    'shuju':shuju
                }
                collection.insert_one(info)