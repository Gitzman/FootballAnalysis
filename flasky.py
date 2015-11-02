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
    return app.send_static_file(makenotebook.editNotebook(start))
