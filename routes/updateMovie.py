'''
Christian Kurdi
Version: 0.1
'''

from flask import Blueprint, render_template, request
from services.movieService import updateMovie, getMovieInfo

updateMovieBP = Blueprint('updateMovie', __name__)

@updateMovieBP.route('/updateMovie')
def showAddMovie():
    return render_template('updateMovie.html')


@updateMovieBP.route('/getMovieInfo')
def get_Movie_Info():
    movieInfo = getMovieInfo()
    return jsonifymovieInfo


@updateMovieBP.route('/updateMovieToDB', methods=['POST'])
def update_Movie():
    name = request.form.get('nameBox')
    genre = request.form.get('genreBox')
    actor1 = request.form.get('actor1')
    actor2 = request.form.get('actor2')
    actor3 = request.form.get('actor3')
    posession = request.form.get('posession')

    check = updateMovie(name, genre, actor1, actor2, actor3, posession)

    if check:
        return render_template('/index.html')
    else:
        return render_template('/updateMovie.html')