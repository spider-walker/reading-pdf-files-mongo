from pymongo import MongoClient
import json

client = MongoClient('mongodb://root:Taifa123*@localhost:27017/admin')

db = client.iebc
voters = db.voters

with open('data/prep-data-to-json.json') as f:
    items = json.load(f)
    for item in items:
        result = voters.insert_one({
            '_id': item,
            item: items[item]
        })
