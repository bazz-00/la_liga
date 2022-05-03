from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///la_liga.db'
db = SQLAlchemy(app)



class Club(db.Model):
    __tablename__ = 'club'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    player = relationship("Player")

    def __repr__(self):
        return f'club {self.name}'


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    role = db.Column(db.String)
    club_id = db.Column(db.Integer, ForeignKey('club.id'))
    club = db.Column(db.String)

    def __repr__(self):
        return f'player {self.name}'


if __name__ == '__main__':
    app.run(debug=True)
