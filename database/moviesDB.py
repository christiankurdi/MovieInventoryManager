'''
Christian Kurdi 
Version: 0.1
'''
import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('movies.db')

    def getCurrentMovies(self):
        statement = "SELECT name FROM movies WHERE owned = 1"
        cursor = self.connection.cursor()
        cursor.execute(statement)
        movies = cursor.fetchall()
        cursor.close()
        return movies
        #add sql statements to get current movies and return values

    def getDesiredMovies(self):
        statement = "SELECT name FROM movies WHERE desired = 1"
        print("success")
        cursor = self.connection.cursor()
        cursor.execute(statement)
        movies = cursor.fetchall()
        cursor.close()
        return movies

    def addAMovie(self, name, genre, actor1, actor2, actor3, owned, desired):
        check = 0
        if actor1 == "":
            actor1 = "Null"
            check = 1
        else:
            actor1 = "\"" + actor1 + "\"" 
        if actor2 == "":
            actor2 = "Null"
        else:
            actor2 = "\"" + actor2 + "\"" 
        if actor3 == "":
            actor3 = "Null"
        else:
            actor3 = "\"" + actor3 + "\"" 
        statement = f'''INSERT INTO movies (name, genre, actor1, actor2, actor3, owned, desired) 
            VALUES
            ("{name}", "{genre}", {actor1}, {actor2}, {actor3}, {owned}, {desired});'''
        
        cursor = self.connection.cursor()
        try:
            cursor.execute(statement)
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            return e
        
    def removeMovie(self, name):
        statement = "DELETE FROM movies WHERE name=" + f"\"{name}\""
        cursor = self.connection.cursor()
        cursor.execute(statement)
        self.connection.commit()
        cursor.close()
        

    def checkMovie(self, name):
        statement = "SELECT name FROM movies WHERE name=" + f"\"{name}\""
        print(statement)
        cursor = self.connection.cursor()
        cursor.execute(statement)
        check = cursor.fetchone()
        print(check)
        if check:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

            
        


    def closeConnection(self):
        self.connection.close()