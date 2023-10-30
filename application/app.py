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
    user_input = request.form["search"]
    # tomma strängar för att undvika fel vid tom input
    topic = ""
    language = ""
    api_lang = ""
    try:
        language = request.form["language"]
        api_lang = "languages=" + language
    except: 
        pass
    try:
        topic = request.form["topic"]
    except:
        pass
    
    api_url = f"https://gutendex.com/books/?search={user_input}&{api_lang}&{topic}"
        

    data = func.json_data_to_html_table(api_url)
    return render_template("table.html", data=data)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html"), 404
