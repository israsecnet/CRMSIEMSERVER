from pymongo import MongoClient
import os

CLIENTURI = os.environ['MONGOURI']


client = MongoClient(CLIENTURI)
db = client["CustomPyLogs"]
collection_name = db["SystemInfoLogs"]
