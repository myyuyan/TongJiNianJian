import os

from bin.digui import init_url

if __name__=='__main__':
    data = {
        'id': 'zb',
        'dbcode': 'hgnd',
        'wdcode': 'zb',
        'm': 'getTree'
    }
    init_url(data=data)