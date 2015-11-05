from flask import Flask
from flask import render_template
import makenotebook
import json
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/3d/<start>")
def thirdd(start):
    return app.send_static_file(makenotebook.grabNotebook(start,7))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
