'''
Christian Kurdi
Version: 0.1
'''

from flask import Blueprint, render_template

homeBP = Blueprint('home', __name__)

@homeBP.route('/')
def showHomePage():
    return render_template('index.html')