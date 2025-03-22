from flask import Flask, render_template, jsonify, abort
import json

app = Flask(__name__)

def load_links():
    with open("links.json", "r") as f:
        return json.load(f)

@app.route("/")
def index():
    links = load_links()
    categories = sorted(set(link.get("category", "Uncategorised") for link in links))
    return render_template("index.html", links=links, categories=categories, current_category=None)

@app.route("/category/<category>")
def category_view(category):
    links = load_links()
    categories = sorted(set(link.get("category", "Uncategorised") for link in links))
    filtered = [link for link in links if link.get("category", "").lower() == category.lower()]
    if not filtered:
        abort(404)
    return render_template("category.html", category=category, links=filtered, categories=categories, current_category=category)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
