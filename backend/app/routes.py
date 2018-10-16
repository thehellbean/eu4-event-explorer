from app import app, event_search
from flask import request
from flask import json


@app.route("/")
@app.route("/index")
def index():
    return "Hello, world!"


@app.route("/search", methods=["GET"])
def search():
    try:
        search_params = json.loads(request.args.get("search"))
    except TypeError:
        return "Invalid search parameters", 400

    search_query = event_search.convert_search_terms_to_xquery(search_params)
    print(search_query)
    events = event_search.search_by_xquery(search_query)
    parsed_events = [event_search.convert_root_to_dict(root) for root in events]
    if len(parsed_events) > 100:
        return json.jsonify(parsed_events[:100])
    return json.jsonify(parsed_events)