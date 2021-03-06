from flask import render_template, Blueprint
from random import randint

views = Blueprint('views', __name__)

@views.route('/lol')
def lol():
    return render_template('lol.html')

@views.route('/pokemon')
def pokemon():
    return render_template('pokemon.html')

@views.route('/familyguy')
def familyguy():
    return render_template('familyguy.html')

@views.route('/games.html')
def games():
    return render_template('games.html')

@views.route('/tvseries.html')
def tvseries():
    return render_template('tvseries.html')

@views.route('/movies.html')
def movies():
    return render_template('movies.html')

@views.route('/random')
def random():
    page=randint(1,3)
    if page ==1:
        return render_template('familyguy.html')
    elif page ==2:
        return render_template('pokemon.html')
    elif page ==3:
        return render_template('lol.html')
