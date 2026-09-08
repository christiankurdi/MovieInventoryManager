'''
Christian Kurdi
Version: 0.1
'''

from flask import Flask
from routes.home import homeBP
from routes.currentMovies import currentMoviesBP
from routes.desiredMovies import desiredMoviesBP
from routes.addMovies import addMovieBP
from routes.removeMovie import removeMovieBP

app = Flask(__name__)

#Register blueprints for webpage navigation
app.register_blueprint(homeBP)
app.register_blueprint(currentMoviesBP)
app.register_blueprint(desiredMoviesBP)
app.register_blueprint(addMovieBP)
app.register_blueprint(removeMovieBP)

if __name__ == "__main__":
    app.run(debug=True)