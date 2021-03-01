from flask import render_template
from . import auth
from flask_login import login_required

@main.route('/')
def index():

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch(id):