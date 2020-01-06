from flask_dance.utils import first
from flask_wtf import FlaskForm
from wtforms import (IntegerField, PasswordField, StringField, SubmitField,
                     ValidationError)
from wtforms.validators import DataRequired, Email, EqualTo
from blog.models import User


class SignupForm(FlaskForm):
    email = StringField('Enter your email : ' , validators=[DataRequired() ,Email() ])
    username = StringField('Enter Username : ' , validators=[DataRequired()] )
    password = PasswordField('Enter Password: ',validators=[DataRequired()] )
    signup = SubmitField("Sign up")

    def check_email_and_username(self):
        error =''
        if User.query.filter_by(email=self.email.data).first() is not None:
            error +='this email is already in use'
        if User.query.filter_by(email=self.username.data).first() is not None:
            error +='this username is already in use'
        if error =='' :
            return True
        else:
            return error


    def check_username(self, field):
        if User.query.filter_by(username=field.data).first() is not None:
            return False
        else:
            return True



class LoginForm(FlaskForm):
    username = StringField('Enter Username : ' , validators=[DataRequired()] )
    password = PasswordField('Enter Password: ', validators=[DataRequired()] )
    login = SubmitField("Log in")