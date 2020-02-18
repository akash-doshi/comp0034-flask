from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class signupForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired(), Length(min=5, max=16)])
   email = StringField('Email address', validators=[DataRequired(), Email()])
   password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=16)])
   submit = SubmitField('Sign Up')