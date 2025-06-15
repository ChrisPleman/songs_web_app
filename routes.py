from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='home')

@app.route('/discover')
def discover():
    return render_template('discover.html', title='Discover')

@app.route('/library')
def library():
    return render_template('library.html', title='My Library')

@app.route('/account')
def account():
    return render_template('account.html', title='My Account')