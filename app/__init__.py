#make config.py in root 
#store key as SECRET_KEY

from config import SECRET_KEY

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
# session.init_app(app)


db = SQLAlchemy(app)

#import tables
from app.models import users


from app.routes import app


with app.app_context():
    db.create_all()
