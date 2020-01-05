from blog import app,db
from flask import render_template, redirect, request, url_for, flash,abort
from blog.forms import LoginForm , SignupForm


@app.route('/', methods=['GET', 'POST'])
def index():
    loginform = LoginForm()
    signupform = SignupForm()
    return render_template('index.html' , loginform = loginform , signupform = signupform )

if __name__ == '__main__':
    app.run(debug=True)
