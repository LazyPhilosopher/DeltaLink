# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
#from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Денис'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
