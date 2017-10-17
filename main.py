from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import datetime

LOCAL = False

from credentials import db_access

app = Flask(__name__)

host='ds033390.mlab.com:33390'
db_name = 'test1'

uri = "mongodb://%s:%s@%s/%s" % (db_access.user, db_access.password, host, db_name)

print(uri)

client = MongoClient(uri)
db = client[db_name]

for x in db.my_posts.find():
    print(x)

@app.route("/")
def page():
    return render_template('index.html')

if LOCAL and __name__ == "__main__":
    app.run(debug=True)
