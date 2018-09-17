from flask import Flask
from lxml import etree as ET
import os

app = Flask(__name__)
db_names = os.listdir("../EU4EventParser/parsed_events")

db_list = [ET.parse("../EU4EventParser/parsed_events/" + i) for i in db_names]

from app import routes, event_search