from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from data_base.sqlal import Player, Club

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_base/la_liga.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '12345'
db = SQLAlchemy(app)


@app.route('/')
def index():
    club = Club.query.all()
    return render_template('index.html', club=club)


@app.route('/about')
def about():
    players = Player.query.order_by(Player.id).all()
    return render_template('about.html', players=players)


@app.route('/<int:fet>')
def real(fet):
    players = Player.query.order_by(Player.id).all()
    club = Club.query.order_by(Club.id).all()
    return render_template('real.html', players=players, club=club, fet=fet)


@app.route('/<int:club_id>/<int:id>')
def real_player(club_id, id):
    reals = Player.query.get(id)
    return render_template('real_player.html', reals=reals)


@app.route('/create_player', methods=['POST', 'GET'])
def create_player():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        role = request.form['role']
        club2 = list(map(str, request.form['club2'].split('-')))
        print(club2)
        player = Player(name=name, number=number, age=age, height=height, weight=weight, role=role, club2=club2[0], club_id=club2[1])
        try:
            db.session.add(player)
            db.session.commit()
            flash('футболист добавлен')
            return redirect('/create_player')
        except:
            return "Ошибка"
    else:
        return render_template('create_player.html')

@app.route('/sort', methods=['POST', 'GET'])
def sort():
    players = Player.query.order_by(Player.name).all()
    return render_template('sort.html', players=players)


if __name__ == '__main__':
    app.run(debug=True)
