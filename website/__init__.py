from os import path
from flask import Flask, render_template, has_request_context, request
from flask_sqlalchemy import SQLAlchemy

__all__ = ['create_app']

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    with app.app_context():
        from .database import initialize_extensions

        initialize_extensions(app)

        from .views import views
        app.register_blueprint(views, url_prefix='/')

    return app