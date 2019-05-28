import os

from bin.digui import init_url

if __name__=='__main__':
    url = 'http://data.stats.gov.cn/easyquery.htm'
    data = {
        'id': 'zb',
        'dbcode': 'hgnd',
        'wdcode': 'zb',
        'm': 'getTree'
    }
    init_url(url=url,data=data)