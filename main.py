from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import datetime
import os

from credentials import db_access

host='ds033390.mlab.com:33390'
db_name = 'test1'

uri = "mongodb://%s:%s@%s/%s" % (db_access.user, db_access.password, host, db_name)

print(uri)

client = MongoClient(uri)
db = client[db_name]

for x in db.my_posts.find():
    print(x)

ON_HEROKU = "ON_HEROKU" in os.environ

app = Flask(__name__)

@app.route("/")
def page():
    return render_template('index.html')

if (not ON_HEROKU) and __name__ == "__main__":
    app.run(debug=True)
