from flask import Flask, render_template, request
import urllib.request
import ssl
import pandas as pd
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/api", methods=["POST"])
def api():
    return render_template("table.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html"), 404
