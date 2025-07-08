from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


# Create a form class
class SearchForm(FlaskForm):
    search_input = StringField("search_input text", validators=[DataRequired()])
    submit = SubmitField("submit field text")
    
# Creating a form to capture users
class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    # todo: Implement the Email validator, and have it flash an error message when an invalid email is submitted
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")