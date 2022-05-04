from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from data_base.sqlal import Player, Club

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///football.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    clubs = Club.query.all()
    return render_template('index.html', clubs=clubs)


@app.route('/about')
def about():
    players = Player.query.order_by(Player.id).all()
    return render_template('about.html', players=players)


@app.route('/real')
def real():
    players = Player.query.order_by(Player.id).all()
    return render_template('real.html', players=players)


@app.route('/real/<int:id>')
def real_player(id):
    reals = Player.query.get(id)
    return render_template('real_player.html', reals=reals)


@app.route('/barcelona')
def barcelona():
    players = Player.query.order_by(Player.id).all()
    return render_template('barcelona.html', players=players)

@app.route('/barcelona/<int:id>')
def barca_player(id):
    reals = Player.query.get(id)
    return render_template('barcelona_player.html', reals=reals)


@app.route('/create_player', methods=['POST', 'GET'])
def create_player():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        role = request.form['role']
        club = request.form['club']
        player = Player(name=name, number=number, age=age, height=height, weight=weight, role=role, club=club)
        try:
            db.session.add(player)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка"
    else:
        return render_template('create_player.html')


if __name__ == '__main__':
    app.run(debug=True)
