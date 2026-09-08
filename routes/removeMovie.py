'''
Christian Kurdi
Version: 0.1
'''

from flask import Blueprint, render_template, request
from services.movieService import removeMovie

removeMovieBP = Blueprint('removeMovie', __name__)

@removeMovieBP.route('/removeMovie')
def showRemoveMovie():
    return render_template('removeMovies.html')


@removeMovieBP.route('/removeFromDB', methods=['POST'])
def remove_Movie():
    name = request.form.get('nameBox')

    success = removeMovie(name)

    if success:
        return render_template('index.html')
    else:
        return render_template('removeMovies.html')