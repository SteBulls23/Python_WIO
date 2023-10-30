from flask import Flask
from .config import config

#flask application factory function
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    return app