from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///la_liga.db'
db = SQLAlchemy(app)


class Club(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Player(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    role = db.Column(db.String)
    club_id = db.Column(db.Integer)
    club = db.Column(db.String)


if __name__ == '__main__':
    app.run(debug=True)
