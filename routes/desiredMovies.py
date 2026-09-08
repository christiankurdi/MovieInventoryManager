'''
Christian Kurdi
Version: 0.1
'''

from flask import Blueprint, render_template, jsonify
from services.movieService import getDesiredMovies

desiredMoviesBP = Blueprint('desiredMovies', __name__)

@desiredMoviesBP.route('/desiredmovies')
def showDesired():
    return render_template('desiredMovies.html')


@desiredMoviesBP.route('/getDesiredMovies')
def getDesired():
    movies = getDesiredMovies()
    return jsonify(movies)