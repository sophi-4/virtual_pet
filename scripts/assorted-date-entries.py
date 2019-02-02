# A script which plants a pile of entries spread across the last 10 days:

from pymongo import MongoClient
import datetime
import random

client = MongoClient()
db = client["dated_items"]
collection = db.items

if True:
    d = datetime.datetime.utcnow()

    for i in range(100):
        post = {"value": random.randint(0, 100),
                "date": d - datetime.timedelta(seconds=random.randint(0, 60*60*24*10))}
        collection.insert_one(post)

# Adapted from: https://docs.mongodb.com/manual/reference/operator/aggregation/group/

def aggregation():
    return collection.aggregate(
        [
            { '$group' : { '_id' : { 'hour' : { "$hour" : "$date" },
                                     'minute' : { "$minute" : "$date" }},
                           'count' : { '$sum' : 1 }}
            }
        ]
    )

print("Aggregration:")

for x in aggregation():
    print(x)


print("Into arrays:")

dataset = [[0 for m in range(60)] for h in range(24)]

for x in aggregation():
    id = x['_id']
    h = id['hour']
    m = id['minute']
    v = x['count']
    dataset[h][m] = v
