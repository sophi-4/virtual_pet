from flask import Flask, request, render_template, jsonify
import datetime
import os

LOCAL = True

ON_HEROKU = "ON_HEROKU" in os.environ

app = Flask(__name__)

@app.route("/")
def page():
    return render_template('index.html')

if (not ON_HEROKU) and __name__ == "__main__":
    app.run(debug=True)
