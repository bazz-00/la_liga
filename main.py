from flask import Flask, render_template, url_for, request, redirect, flash, make_response, session
from flask_sqlalchemy import SQLAlchemy
from data_base.sqlal import Player, Club, User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_base/la_liga.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '12345'
db = SQLAlchemy(app)
list_role = ['вратарь', 'защитник', 'полузащитник', 'нападающий']


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

        player = Player(name=name, number=number, age=age, height=height, weight=weight, role=role, club2=club2[0],
                        club_id=club2[1])
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
    if request.method == 'POST':
        if request.form.get('number') == 'number':
            players = Player.query.order_by(Player.number).all()
        elif request.form.get('name') == 'name':
            players = Player.query.order_by(Player.name).all()
        elif request.form.get('age') == 'age':
            players = Player.query.order_by(Player.age).all()
        elif request.form.get('height') == 'height':
            players = Player.query.order_by(Player.height).all()
        elif request.form.get('weight') == 'weight':
            players = Player.query.order_by(Player.weight).all()
        elif request.form.get('role') == 'role':
            players = Player.query.order_by(Player.role).all()
        elif request.form.get('club') == 'club':
            players = Player.query.order_by(Player.club2).all()
        elif request.form.get('role2'):
            for i in list_role:
                if i == request.form.get('role2'):
                    players = Player.query.filter_by(role=i).all()
    return render_template('sort.html', players=players)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if len(request.form['email']) > 4 and len(request.form['psw']) > 4 \
                and request.form['psw'] == request.form['psw']:
            hash = generate_password_hash(request.form['psw'])
            user = User(name=request.form['name'], email=request.form['email'], password=hash)
            try:
                db.session.add(user)
                db.session.commit()
                flash('вы зарегистрированы')
                return redirect('/login')
            except:
                return "Ошибка"
        else:
            return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
