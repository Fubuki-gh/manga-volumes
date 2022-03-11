from flask import Flask
from flask_restful import Api

from API.models.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

db.init_app(app)

from API.resources.title import TitleSearch
from API.resources.title import Title

# Search
api.add_resource(TitleSearch, '/search/title', resource_class_kwargs={'db': db})

# Get
api.add_resource(Title, '/title/<int:id>', resource_class_kwargs={'db': db})