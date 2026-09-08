'''
Christian Kurdi
Version: 0.1
'''

from flask import Blueprint, render_template, jsonify
from services.movieService import getCurrentMovies

currentMoviesBP = Blueprint('currentMovies', __name__)

@currentMoviesBP.route('/currentmovies')
def showCurrent():
    return render_template('currentMovies.html')


@currentMoviesBP.route('/getCurrentMovies')
def getCurrent():
    movies = getCurrentMovies()
    return jsonify(movies)
