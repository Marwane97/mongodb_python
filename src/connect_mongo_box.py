from dotenv import load_dotenv
import pymongo
import os

load_dotenv()

mongo_host = os.getenv('mongo_host')
mongo_port = os.getenv('mongo_port')
mongo_collection = os.getenv('mongo_collection')
mongo_database = os.getenv('mongo_database')

mongo_client = pymongo.MongoClient('mongodb://' + mongo_host + ':' + mongo_port + '/')

mongo_client_database = mongo_client[mongo_database]

collection = mongo_client_database[mongo_collection]


