from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Integer, Column
from sqlalchemy.orm import relationship
import data_base.parsing
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///la_liga.db'
db = SQLAlchemy(app)
engine = create_engine('sqlite:///la_liga.db', echo=False)
#a = data_base.parsing.sports_ru("https://www.sports.ru/real/team/")  # you need to change the names of commands to add to the table


class Club(db.Model):
    __tablename__ = 'club'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    players = relationship("Player", backref='club', lazy='dynamic')

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
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'))
    club2 = db.Column(db.String)

    def __repr__(self):
        return f'player {self.name}'





# Session = sessionmaker(bind=engine)
# session = Session()
# c = ['Алавес', 'Атлетик Бильбао', 'Атлетико Мадрид', 'Барселона', 'Бетис', 'Севилья', 'Валенсия', 'Вильярреал',
#       'Гранада', 'Кадис', 'Леванте', 'Мальорка', 'Осасуна', 'Райо Вальекано', 'Реал Сосьедад', 'Сельта', 'Хетафе',
#      'Эльче', 'Эспаньол', 'Реал Мадрид']
# for i in c:
#     c1 = Club(name=i)
#     session.add(c1)
# session.commit()
# Session = sessionmaker(bind=engine)
# session = Session()
# for i in a:
#     c1 = Player(number=i[0], name=i[1][2:-1], age=i[2], height=i[3], weight=i[4], role=i[5], club_id=20, club2='Real Madrid')
#     session.add(c1)
#
# session.commit()

if __name__ == '__main__':
    app.run(debug=True)
