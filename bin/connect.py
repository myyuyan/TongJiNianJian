import pymongo
from conf.config import *
def connect():
    client = pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)