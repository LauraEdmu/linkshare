from flask import Flask, render_template, jsonify, abort, send_file, redirect
import os
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

### File Serving ###

@app.route("/zshrc")
def serve_zshrc():
    filepath = os.path.expanduser("~/.zshrc")
    if os.path.isfile(filepath):
        return send_file(filepath, mimetype="text\plain", as_attachment=False)
    else:
        abort(404)

@app.route("/ssh")
def serve_sshkey():
    filepath = os.path.expanduser("~/web/orca.pub")
    if os.path.isfile(filepath):
        return send_file(filepath, mimetype="text\plain", as_attachment=False)
    else:
        abort(404)

@app.route("/nezumi")
def serve_sshkey_nezumi():
    filepath = os.path.expanduser("~/web/nezumi.pub")
    if os.path.isfile(filepath):
        return send_file(filepath, mimetype="text\plain", as_attachment=False)
    else:
        abort(404)

@app.route("/volunteer")
def serve_volunteer_pdf():
    filepath = os.path.join(os.path.dirname(__file__), "static", "volunteer.pdf")
    if os.path.isfile(filepath):
        return send_file(filepath, mimetype="application/pdf", as_attachment=True)
    else:
        abort(404)

### Redirects ###

@app.route("/git")
def git_redirect():
    return redirect("https://github.com/LauraEdmu", code=302)

@app.route("/admin")
def rick_r():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.route("/win")
def massgrave():
    return redirect("https://get.activated.win")

### Full Pages ###

@app.route("/discord")
def discord():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My Discord</title>
        <style>
            body {
                background-color: #1e1e1e;
                color: #e0e0e0;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                padding-top: 4em;
            }
            .container {
                background: #2a2a2a;
                border-radius: 1em;
                display: inline-block;
                padding: 2em 3em;
                box-shadow: 0 0 12px #00000088;
            }
            img {
                width: 96px;
                height: 96px;
                border-radius: 50%;
                margin-bottom: 1em;
                border: 2px solid #7289da;
            }
            .discord-name {
                font-size: 1.5em;
                letter-spacing: 0.5px;
                color: #ffffff;
                margin-top: 0.25em;
            }
            .note {
                font-size: 0.95em;
                color: #aaaaaa;
                margin-top: 0.5em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://cdn.discordapp.com/avatars/262687596642041856/81a5aee1eb4b658933443833fded622d?size=1024" alt="My PFP">
            <div class="discord-name" id="discord-username">Loading…</div>
            <div class="note">Add me on Discord</div>
        </div>
        <script>
            // JS obfuscation for light bot protection
            const part1 = "iced";
            const part2 = "phoenix";
            document.getElementById("discord-username").innerText = part1 + part2;
        </script>
    </body>
    </html>
    '''

@app.route("/github")
def github():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My GitHub</title>
        <style>
            body {
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: 'Segoe UI', 'Liberation Sans', Arial, sans-serif;
                text-align: center;
                padding-top: 4em;
            }
            .container {
                background: #161b22;
                border-radius: 1em;
                display: inline-block;
                padding: 2em 3em;
                box-shadow: 0 0 16px #010409cc;
                border: 1px solid #30363d;
            }
            img {
                width: 96px;
                height: 96px;
                border-radius: 50%;
                margin-bottom: 1em;
                border: 2px solid #30363d;
                background: #010409;
            }
            .github-name {
                font-size: 1.5em;
                letter-spacing: 0.5px;
                color: #58a6ff;
                margin-top: 0.25em;
                font-weight: 600;
            }
            .github-name a {
                color: #58a6ff;
                text-decoration: none;
                transition: color 0.2s;
            }
            .github-name a:hover {
                color: #79c0ff;
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://avatars.githubusercontent.com/u/98789693?v=4" alt="My PFP">
            <div class="github-name" id="github-username">
                <a href="https://github.com/LauraEdmu" target="_blank" rel="noopener">LauraEdmu</a>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8050)

