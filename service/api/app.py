import sqlite3
from flask import Flask
from flask_restful import Api
from api.resources.title import TitleSearch


app = Flask(__name__)
api = Api(app)
db = sqlite3.connect('../database/database.sqlite3', check_same_thread=False)

api.add_resource(TitleSearch, '/title/search', resource_class_kwargs={'db': db})
