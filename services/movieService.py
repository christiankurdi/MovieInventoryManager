'''
Christian Kurdi
Version: 0.1
'''

from database.moviesDB import Database

def getCurrentMovies():
    connection = Database()
    movies = connection.getCurrentMovies()
    connection.closeConnection()
    return movies

def getDesiredMovies():
    connection = Database()
    movies = connection.getDesiredMovies()
    connection.closeConnection()
    return movies

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
    check = connection.addMovie(name, genre, actor1, actor2, actor3, own, want)
    connection.closeConnection()
    return check

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