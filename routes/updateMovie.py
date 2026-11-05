'''
Christian Kurdi
Version: 0.1
'''

from flask import Blueprint, render_template, request, jsonify
from services.movieService import updateMovie, getMovieInfo

updateMovieBP = Blueprint('updateMovie', __name__)

@updateMovieBP.route('/updateMovie')
def showAddMovie():
    return render_template('updateMovie.html')


@updateMovieBP.route('/getMovieInfo')
def get_Movie_Info():
    name = request.args.get('name')#Gets the name from the url called from javascript
    movieInfo = getMovieInfo(name)#Database call
    return jsonify(movieInfo)


@updateMovieBP.route('/updateMovieToDB', methods=['POST'])
def update_Movie():
    oldName = request.form.get('oldName')
    newName = request.form.get('nameBox')
    genre = request.form.get('genreBox')
    actor1 = request.form.get('actor1')
    actor2 = request.form.get('actor2')
    actor3 = request.form.get('actor3')
    posession = request.form.get('posession')

    check = updateMovie(oldName, newName, genre, actor1, actor2, actor3, posession)

    if check:
        return render_template('index.html')
    else:
        return render_template('updateMovie.html')