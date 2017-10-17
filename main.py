from flask import Flask, request, render_template, jsonify
import datetime

LOCAL = False

app = Flask(__name__)

@app.route("/")
def page():
    return render_template('index.html')

if LOCAL and __name__ == "__main__":
    app.run(debug=True)
