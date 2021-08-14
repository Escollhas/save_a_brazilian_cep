import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from environs import Env

db = SQLAlchemy()
ma = Marshmallow()

def init_app(app):
    env = Env()
    basedir = os.path.abspath(os.path.dirname(__file__))[:-11]
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False
    db.init_app(app)
    ma.init_app(app)
    app.db = db
    from app.models.cep_model import CepModel