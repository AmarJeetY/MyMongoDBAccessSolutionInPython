import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://YourUserName:<YourPassword>@cluster0.myezt.mongodb.net/<YourDBName>?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]
post = {"_id": 0, "name": "Amarjeet", "score": 100}
collection.insert_one(post)
