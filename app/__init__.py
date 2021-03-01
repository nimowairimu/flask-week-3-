from flask import Flask 
from flask_bootstrap import Bootstrap
from app import error
from flask_sqlalchemy import SQLAlchemy
from .config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

from app import views    