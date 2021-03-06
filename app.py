#!/usr/bin/python3

import os
from enum import unique
from click import password_option
from flask import Flask, render_template, redirect, flash, url_for
from flask_login import LoginManager, login_required, logout_user, login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

from config import Config

import threading

import mqtt
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

#import motor
#import epaper

POOL_TIME = 5

dataDo = 0
dataLock = threading.Lock()
actionThread = threading.Thread()  
login_manager = LoginManager()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/aquapi.sqlite'
db = SQLAlchemy(app)

class AquaUser(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String, nullable=False, unique=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
    created = db.Column(db.Time, nullable=True)

    @property
    def is_active(self):
        return self.active
    
    def __repr__(self):
        return '<User %r>' % self.username

class AquaConfig(db.Model):
    __tablename__ = 'config'
    id = db.Column(db.Integer, primary_key=True)
    mqtt_host = db.Column(db.String, nullable=False, unique=True)
    mqtt_port = db.Column(db.Integer, nullable=False, unique=True, default=1883)
    mqtt_topic = db.Column(db.String, nullable=False, unique=True)
    config_date = db.Column(db.Date, nullable=False, unique=True)
    created = db.Column(db.Time, nullable=True)

class AquaLight(db.Model):
    __tablename__ = 'light'
    id = db.Column(db.Integer, primary_key=True)
    lightchannel = db.Column(db.Integer, nullable=False)
    lightminute = db.Column(db.Integer, nullable=False)
    lightvalue = db.Column(db.SmallInteger, nullable=False)

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
    user = AquaUser(id=user_id)
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
def aquausers():
    return render_template('users.html')

@app.route("/overview", methods=['GET', 'POST'])
def myindex():
    return render_template('overview.html', configs=myconfig)
    #return render_template('overview.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        formusername = form.user_name.data
        user = AquaUser.query.filter_by(username=formusername).first()

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

db.create_all()

if not AquaUser.query.filter_by(username='admin').first():
    admin = AquaUser(username='admin', email='admin@example.com', password = 'asdf')
    db.session.add(admin)
if not AquaUser.query.filter_by(username='guest').first():
    guest = AquaUser(username='guest', email='guest@example.com', password='')
    db.session.add(guest)
db.session.commit()

if not AquaLight.query.count() > 0:
    lightup = AquaLight(lightchannel=1, lightminute=0, lightvalue=255)
    db.session.add(lightup)
    lightdown = AquaLight(lightchannel=1, lightminute=60*12, lightvalue=0)
    db.session.add(lightdown)
db.session.commit()

myconfig = AquaConfig.query.first()
if not myconfig:
    myconfig = AquaConfig(mqtt_host='127.0.0.1', mqtt_port='1883', mqtt_topic = '/aquapi')
else: myconfig = AquaConfig.query().first()
db.session.commit()

actionThread = threading.Timer(POOL_TIME, actionDo, ())
actionThread.start()  

app.config.from_object(AquaConfig)

login_manager.init_app(app)

mqtt.mqttconnect(myconfig.mqtt_host, myconfig.mqtt_port)
   
app.run(debug=True, use_debugger=True, use_reloader=False)
