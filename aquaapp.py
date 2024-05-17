#!/usr/bin/python3

import os
import importlib

from enum import unique
from click import password_option
from flask import Flask, render_template, redirect, flash, url_for
from flask_login import LoginManager, login_required, logout_user, login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

global aqua_db

import gettext #localisations

applocale = gettext.translation('base', localedir='locales/',languages=['cs'])
applocale.install()
_ = applocale.gettext

#discover and init in configuration enabled plugins like motor,epaper,mqtt
#foreach importlib.search....
module = importlib.find_loader('PluginMQTT', 'plugins')
mymodule = importlib.import_module('plugins.pluginMQTT')
myclass = getattr(mymodule, 'PluginMQTT')
myobject = myclass()
myobject.readconfig()
myobject.load()

from flask_login import UserMixin

POOL_TIME = 5

login_manager = LoginManager()

app = Flask(__name__, template_folder='static/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aquapi.sqlite'
app.app_context().push()

aqua_db = SQLAlchemy()
aqua_db.init_app(app)
aqua_db.create_all()

import aquaconfig
import aquauser

@login_manager.user_loader
def load_user(user_id):
    user = aquauser.aquaUser(id=user_id)
    return user

@app.route("/configure", methods=['GET', 'POST'])
@login_required
def configure():
    return render_template('configure.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/users')
def aquausers():
    return render_template('users.html')

@app.route("/overview", methods=['GET', 'POST'])
def myindex():
    return render_template('overview.html', configs=aquaconfig.aquaConfig)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        formusername = form.user_name.data
        user = aquauser.aquaUser.query.filter_by(username=formusername).first()

        if user.password == form.password.data:
            login_user(user)
            flash('Logged in successfully.')
            return redirect('/overview')
        else:
            print("bad password for user \n" + user.username) 
            flash('Bad password.')

        
    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')
 
class Config(object):
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

class LoginForm(FlaskForm):
    user_name = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

app.config.from_object(aquaconfig.aquaConfig)

login_manager.init_app(app)
   
app.run(debug=True, use_debugger=True, use_reloader=False)
