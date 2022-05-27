#!/usr/bin/python3

import time
import sqlite3
import flask
from flask import Flask, render_template, redirect, flash, url_for
from flask_login import LoginManager, UserMixin, login_required, logout_user, login_user

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

from config import Config

import app

class Config(object):
    SECRET_KEY = 'my-secrete-key' 

class LoginForm(FlaskForm):
    user_name  = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

conn = sqlite3.connect('aquapi.db')
conn.row_factory = sqlite3.Row    
configs = conn.execute('SELECT * FROM aquapi').fetchall()
conn.close()

login_manager = LoginManager()

print(configs)

app = Flask(__name__)

app.config.from_object(Config)

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    
    return UserMixin.get(user_id)

@app.route("/configure", methods=['GET', 'POST'])
@login_required
def configure():
    return render_template('configure.html', configs=configs)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', configs=configs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = UserMixin()
        login_user(user)

        flash('Logged in successfully.')

        next = flask.request.args.get('next')

        if not flask.is_safe_url(next):
            return flask.abort(400)

        return redirect(next or url_for('/'))
    return render_template('login.html', form=form)
    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('/login'))
