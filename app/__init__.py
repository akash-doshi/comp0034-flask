from flask import Flask, render_template, flash, redirect, url_for
from os.path import dirname, abspath, join
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from config import DevConfig

def create_app(config_class=DevConfig):
    """
    Creates an application instance to run using settings from config.py
    :return: A Flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = "dfdQbTOExternjy5xmCNaA"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CWD = dirname(abspath(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(CWD, 'rain.sqlite')

    # Initialise the database and create tables
    db.init_app(app)

    # The following is needed if you want to map classes to an existing database
    with app.app_context():
        db.Model.metadata.reflect(db.engine)

        # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app
