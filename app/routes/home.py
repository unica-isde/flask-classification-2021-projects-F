from flask import render_template

from app import app
from config import Configuration

conf = Configuration()


@app.route('/home', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    ''' 
    Render home.html page
    '''
    return render_template('home.html')
