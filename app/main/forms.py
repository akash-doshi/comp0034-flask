from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from werkzeug.routing import ValidationError
from wtforms.validators import DataRequired, Email, Length

from app.models import User


class searchForm(FlaskForm):
   city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])
   submit = SubmitField('Search')

class signupForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired(), Length(min=5, max=16)])
   email = StringField('Email address', validators=[DataRequired(), Email()])
   password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=16)])
   submit = SubmitField('Sign Up')


def validateEmail(self, email):
   user = User.query.filter_by(email=email.data).first()
   if user is not None:
      raise ValidationError('An account already exists for this email address.')