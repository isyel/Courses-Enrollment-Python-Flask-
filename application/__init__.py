from flask import Flask
from config import Config
from flask_restx import Api
from flask_mongoengine import MongoEngine

api = Api()

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)
api.init_app(app)

from application import routes