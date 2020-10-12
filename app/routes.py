from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/index')
def index():
    user = {'username': 'guest'}
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
            'author': {'username': 'Confucius'},
            'body': 'Seryi is baklan'
        },
        {
            'author': {'username': 'admin'},
            'body': 'website test commencing...'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)