from pymongo import MongoClient
import datetime

from credentials import db_access

host='ds033390.mlab.com:33390'
db_name = 'test1'
uri = "mongodb://%s:%s@%s/%s" % (db_access.user, db_access.password, host, db_name)

client = MongoClient(uri)
db = client[db_name]

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

collection = db.my_posts
collection.insert_one(post)

for x in db.my_posts.find():
    print(x)
