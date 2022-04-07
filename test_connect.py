from pymongo import MongoClient

conn = MongoClient("localhost", 27017)
db = conn.local
collection = db.test

# This deletes all! run at start to clear all
collection.delete_many({})

info = {
    "name": "Oliver",
    "age": 33,
    "score": 5
}

# add one
collection.insert_one(info)

info1 = {
    "name": "Graham",
    "age": 15,
    "score": 2
}

info2 = {
    "name": "John",
    "age": 82,
    "score": 5
}

info3 = {
    "name": "Terry",
    "age": 77,
    "score": 4
}

# add many
collection.insert_many([info1, info2, info3])

# update existing once
collection.update_one({'name': 'Terry'}, {"$set":{"age": 40}})
# update existing many
collection.update_many({'name': 'Terry'}, {"$set":{"age": 40}})
# update existing many ($inc so adds 5 to age)
collection.update_many({'name': 'Terry'}, {"$inc":{"age": 5}})


read_back = collection.find()
for item in read_back:
    print(item)

