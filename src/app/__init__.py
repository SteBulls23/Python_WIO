from flask import Flask
from .config import config
from src.app.main.views import main
from src.app.api.rest_api import api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#flask application factory function
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.json.sort_keys = False
    db.init_app(app)
    app.register_blueprint(main, url_prefix = "/main")
    app.register_blueprint(api, url_prefix = "/api")
    return app