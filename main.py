from flask import Flask, request, render_template, jsonify, send_from_directory
from pymongo import MongoClient
import datetime
import os

ON_HEROKU = "ON_HEROKU" in os.environ

if ON_HEROKU:
    from credentials import db_hosted
    db = db_hosted
    uri = "mongodb://%s:%s@%s/%s" % (db.user, db.password, db.host, db.db_name)
else:
    from credentials import db_local
    db = db_local
    uri = "mongodb://%s/%s" % (db.host, db.db_name)

print(uri)

client = MongoClient(uri)
db = client[db.db_name]

app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/exchange', methods=['POST'])
def exchange():
    json = request.get_json()
    if json['data'] == 37:
        return jsonify({ 'x' : 56, 'y' : [-200, 55], 'thirty_seven': 'YES'  })
    else:
        return jsonify({ 'x' : 56, 'y' : [-200, 55], 'z' : json['data']  })

@app.route('/add_data', methods=['POST'])
def add_data():
    json = request.get_json()
    instruction = json['instruction']
    mood = json['mood']

    id = db.my_posts.insert_one({'instruction': instruction,
                                 'mood': mood,
                                 'timestamp': datetime.datetime.utcnow()})

    print(id)
    return jsonify({'status' : 'DONE'})

@app.route("/")
def page():
    return render_template('index.html', data=db.my_posts.find())

if (not ON_HEROKU) and __name__ == "__main__":
    app.run(debug=True)
