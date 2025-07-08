from app import app
from flask import render_template
import forms


# Pass stuff to the Navbar (in a nested extended template file navbar.html)
@app.context_processor
def base():
    form = forms.SearchForm()
    return dict(form=form)

@app.route('/search', methods=['POST'])
def search():
    form = forms.SearchForm()
    
    if form.validate_on_submit():
        post_search_input = form.search_input.data
        return render_template("search.html", form=form, search_input=post_search_input)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home():
    
    # # Creating a variable for the search_input attribute in SearchForm class
    # search_input = None
    
    # # Creating an instance of the SearchForm class
    # form = forms.SearchForm()
    
    # # Validate form
    # if form.validate_on_submit():
    #     # Assigning user input to this field
    #     search_input = form.search_input.data
        
    #     # Clearing the form input
    #     form.search_data.data = ''
    
    return render_template('index.html', title='home'#, search_input=search_input, form=form
                           )
    
# Creating a route specifically for adding a user: The specific path is derived from this video: https://www.youtube.com/watch?v=Q2QmST-cSwc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&index=8
@app.route('/user/add')
def add_user():
    return render_template('add_user.html', title='Login')

@app.route('/discover')
def discover():
    return render_template('discover.html', title='Discover')

@app.route('/library')
def library():
    return render_template('library.html', title='My Library')

@app.route('/account')
def account():
    return render_template('account.html', title='My Account')