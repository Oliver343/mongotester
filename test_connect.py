from pymongo import MongoClient

conn = MongoClient("localhost", 27017)
db = conn.local
collection = db.test

info = {
    "name": "Oliver",
    "age": 33,
    "score": 5
}

collection.insert_one(info)
