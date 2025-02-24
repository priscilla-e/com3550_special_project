from flask import Flask
from config import Config


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(flask_app):
    from app.extensions import cors

    cors.init_app(flask_app)


def register_blueprints(flask_app):
    from app.gpt import gpt_bp

    flask_app.register_blueprint(gpt_bp, url_prefix='/api')
