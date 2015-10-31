from flask import Flask
from flask import render_template
import makenotebook
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/3d/<start>")
def tweets(start):
    return app.send_static_file(makenotebook.editNotebook(start))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
