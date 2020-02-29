from django.conf import settings
from pymongo import MongoClient


def connect_mongo(host=settings.MONGO_HOST, db=settings.MONGO_DB, port=settings.MONGO_PORT, username=settings.MONGO_USER, password=settings.MONGO_PASSWORD):
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (
            username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db]
