from flask import Flask, render_template, request, make_response
import json
from application import func

app = Flask(__name__)

@app.route("/")
def index():
    message = "Välkommen idk fixa det här"
    return render_template("index.html", message=message)

@app.route("/form")
def form():

    with open("static/languages.json", "r", encoding="utf-8") as f:
        langs = json.load(f)
    with open("static/topics.json", "r", encoding="utf-8") as f:
        topics = json.load(f)

    # To auto select previous search options
    previous_search = request.cookies.get("search_query", "")
    previous_topic = request.cookies.get("topic", "")
    previous_language = request.cookies.get("language", "")

    return render_template("form.html", langs=langs, topics=topics, previous_search=previous_search, previous_topic=previous_topic, previous_language=previous_language)

@app.route("/api", methods=["POST"])
def api_post():
    # Get users input
    user_input = request.form.get("search_query", "").strip()  # Using strip to remove any leading/trailing spaces
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

    tuple_data = func.json_data_to_html_table(api_url)
    if isinstance(tuple_data, tuple):
        data, next_link = tuple_data
    else:
        data = tuple_data
        next_link = None
    # Set or update the cookies
    resp = make_response(render_template("table.html", data=data, next_link=next_link))
    resp.set_cookie("search_query", user_input)
    resp.set_cookie("topic", topic)
    resp.set_cookie("language", language)

    return resp  # Return the response with the cookies and renders the template to show data

# View next page of results
@app.route("/api_next", methods=["POST"])
def api_next():
    api_url = request.form.get("next")

    tuple_data = func.json_data_to_html_table(api_url)
    if isinstance(tuple_data, tuple):
        data, next_link = tuple_data
    else:
        data = tuple_data
        next_link = None

    return render_template("table.html", data=data, next_link=next_link)
@app.route("/error")
def no_results_found():
    return render_template("error.html")



@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html"), 404