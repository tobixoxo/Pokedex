from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # we don't need real time updates as this is a REST based api
db = SQLAlchemy(app)


from backend.models import *
db.create_all()

from backend import routes


