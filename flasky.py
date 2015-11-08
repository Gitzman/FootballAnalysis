from flask import Flask
from flask import render_template
import makenotebook
import json
import os
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/adhoc")
def adhoc():
    return app.send_static_file(request.args.get('art')+".html")

@app.route("/3d")

def thirdd():
    start=request.args.get('start')
    end=request.args.get('end')
    return app.send_static_file(makenotebook.grabNotebook(start,end))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
