'''
Christian Kurdi
Version: 0.1
'''

from database.moviesDB import Database

#Method to get list of current movies
def getCurrentMovies():
    connection = Database()
    movies = connection.getCurrentMovies()
    connection.closeConnection()
    return movies

#Method to get list of desired movies
def getDesiredMovies():
    connection = Database()
    movies = connection.getDesiredMovies()
    connection.closeConnection()
    return movies

#Method to get a movie's information, still need to account for movies with the same name
def getMovieInfo(name):
    connection = Database()
    movieInfo = connection.getMovieInfo(name)
    connection.closeConnection()
    return movieInfo

#Method to update a movie's information
def updateMovie(name, genre, actor1, actor2, actor3, own, want):
    connection = Database()
    check = connection.updateAMovie(name, genre, actor1, actor2, actor3, own, want)
    connection.closeConnection()
    return check

#Method to add a movie to database
def addMovie(name, genre, actor1, actor2, actor3, posession):
    own = 0
    want = 0

    # should change to switch
    if genre == "0":
        genre == None
    if posession == "0":
        own = 1
    elif posession == "1":
        want = 1

    connection = Database()
    check = connection.addAMovie(name, genre, actor1, actor2, actor3, own, want)
    connection.closeConnection()
    return check

#Method to remove movie from database
def removeMovie(name):
    connection = Database()
    check = connection.checkMovie(name)

    if check:
        connection.removeMovie(name)
        connection.closeConnection()
        return True
    else:
        connection.closeConnection()
        return False