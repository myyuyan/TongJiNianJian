import pymongo
from conf.config import *
def connect():
    client = pymongo.MongoClient()