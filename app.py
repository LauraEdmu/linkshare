from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Load links from JSON file initially
with open("links.json", "r") as f:
    links = json.load(f)

@app.route("/")
def index():
    with open("links.json", "r") as f:
        links = json.load(f)
    return render_template("index.html", links=links)


@app.route("/api/links")
def api_links():
    return jsonify(links)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
