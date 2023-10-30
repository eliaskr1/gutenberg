from flask import Flask, render_template, request
import urllib.request
import ssl
import pandas as pd
import json
from application import func

app = Flask(__name__)

@app.route("/")
def index():
    with open('static/languages.json', "r", encoding="utf-8") as f:
        data = json.load(f)
    return render_template("index.html", data=data)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/api", methods=["POST"])
def api_post():
    user_input = request.form.get("search", "").strip()  # Using strip to remove any leading/trailing spaces
    topic = request.form.get("topic", "").strip()
    language = request.form.get("language", "").strip()

    # Create a list to store valid query parameters
    params = []

    # Add search keyword if it's present
    if user_input:
        params.append(f"search={user_input}")

    # Add language if it's present
    if language:
        params.append(f"languages={language}")

    # Add topic if it's present
    if topic:
        params.append(f"topic={topic}")

    # Form the API URL
    base_url = "https://gutendex.com/books/"
    api_url = f"{base_url}?{'&'.join(params)}"

    data = func.json_data_to_html_table(api_url)
    return render_template("table.html", data=data)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html"), 404
