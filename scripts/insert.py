from pymongo import MongoClient
import datetime
import random

client = MongoClient()
db = client["mytable"]

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "random_no" : random.randint(0, 100),
        "date": datetime.datetime.utcnow()}

collection = db.my_posts
collection.insert_one(post)

for x in db.my_posts.find():
    print(x)
