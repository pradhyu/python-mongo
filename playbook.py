import pymongo

from pymongo import MongoClient
user="root"
password="WVdKc2RsUlBORFZaTlE9PQ=="

client = MongoClient(host="localhost",username=user, port=27017, password=password, authSource='the_database',authMechanism='SCRAM-SHA-1')
for col in client.database_names:



