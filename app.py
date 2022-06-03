#!/usr/bin/python3

from flask import Flask, render_template, redirect, flash, url_for
from flask_login import LoginManager, UserMixin, login_required, logout_user, login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

from config import Config

#import app
import threading

import dbaccess
import mqtt
#import motor
#import epaper

POOL_TIME = 5

dataDo = 0
myconfig = dbaccess.dbgetconfig()
dataLock = threading.Lock()
actionThread = threading.Thread()  
login_manager = LoginManager()

app = Flask(__name__)

def actionDo():

    global dataDo

    print(dataDo, 'Read temperature...')
    print(dataDo, 'Read watter level...')
    print(dataDo, 'Redraw info display...')
    
    print(dataDo, 'Setup lights...')
    print(dataDo, 'Publish mqtt data...')
    dataDo = dataDo + 1

    actionThread = threading.Timer(POOL_TIME, actionDo, ())
    actionThread.start()

@login_manager.user_loader
def load_user(user_id):
    user = UserMixin()
    user.id = user_id
    user.email = 'asdf@asdf.cz'
    return user

@app.route("/configure", methods=['GET', 'POST'])
@login_required
def configure():
    return render_template('configure.html')

@app.route("/")
def index():
    # return redirect('/index.html')
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route("/overview", methods=['GET', 'POST'])
def myindex():
    #return render_template('overview.html', configs=configs)
    return render_template('overview.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = UserMixin()
        user.id = 1
        login_user(user)

        flash('Logged in successfully.')

        return redirect('/overview')
    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')
 
class Config(object):
    SECRET_KEY = 'my-secrete-key'

class LoginForm(FlaskForm):
    user_name = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

actionThread = threading.Timer(POOL_TIME, actionDo, ())
actionThread.start()  

app.config.from_object(Config)

login_manager.init_app(app)

mqtt.mqttconnect(myconfig['mqtt_host'], myconfig['mqtt_port'])
   
app.run(debug=True, use_debugger=True, use_reloader=False)
