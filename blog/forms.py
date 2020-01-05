from flask_dance.utils import first
from flask_wtf import FlaskForm
from wtforms import (IntegerField, PasswordField, StringField, SubmitField,
                     ValidationError)
from wtforms.validators import DataRequired, Email, EqualTo


class SignupForm(FlaskForm):
    email = StringField('Enter your email : ' , validators=[DataRequired() ,Email() ])
    username = StringField('Enter Username : ' , validators=[DataRequired()] )
    password = PasswordField('Enter Password: ',validators=[DataRequired(), EqualTo('pass_confirm', message='passwords must match!') ] )
    pass_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()] )
    submit = SubmitField("Sign up")

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email is taken')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username is taken')


class LoginForm(FlaskForm):
    username = StringField('Enter Username : ' , validators=[DataRequired()] )
    password = PasswordField('Enter Password: ', validators=[DataRequired()] )
    submit = SubmitField("Log in")