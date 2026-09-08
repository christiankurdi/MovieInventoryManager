'''
Christian Kurdi
Version: 0.1
'''

from flask import Blueprint, render_template, request
from services.movieService import addMovie

addMovieBP = Blueprint('addMovie', __name__)

@addMovieBP.route('/addMovie')
def showAddMovie():
    return render_template('addMovies.html')


@addMovieBP.route('/addMovieToDB', methods=['POST'])
def add_Movie():
    name = request.form.get('nameBox')
    genre = request.form.get('genreBox')
    actor1 = request.form.get('actor1')
    actor2 = request.form.get('actor2')
    actor3 = request.form.get('actor3')
    posession = request.form.get('posession')

    check = addMovie(name, genre, actor1, actor2, actor3, posession)

    if check:
        return render_template('/addMovies.html')
    else:
        return render_template('index.html')