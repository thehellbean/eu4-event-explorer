from app import app, db_list, event_search

@app.route("/")
@app.route("/index")
def index():
    return "Hello, world!"


@app.route("/search")
def search():
    root = db_list[0].xpath("//parameter[@name='country_event']")[0]
    return event_search.convert_root_to_json(root)
