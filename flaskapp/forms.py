"""Forms to render HTML input & validate request data."""

from wtforms import BooleanField, DateTimeField, PasswordField
from wtforms import TextAreaField, StringField
from wtforms.validators import Length, DataRequired
from wtforms import validators
from flask_wtf import Form
from wtforms.fields import SubmitField


class LoginForm(Form):
    """Render HTML input for user login form.
    Authentication (i.e. password verification) happens in the view function.
    """
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])
