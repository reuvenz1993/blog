from blog import app,db
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user
from blog.forms import LoginForm , SignupForm
from blog.models import User


@app.route('/', methods=['GET', 'POST'])
def index():
    loginform = LoginForm()
    signupform = SignupForm()
    error = ''
    msg = ''

    return render_template('index.html' , loginform = loginform , signupform = signupform , error = error , msg=msg )

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('login run')
    loginform = LoginForm()
    signupform = SignupForm()
    error = ''
    msg = False
    if loginform.login.data and loginform.validate_on_submit():
        logged_in_user = User.query.filter_by(username=loginform.username.data).first()
        if ( logged_in_user is not None and logged_in_user.check_password(loginform.password.data) ) :
            print (logged_in_user)
            login_user(logged_in_user)
            return redirect(url_for('home'))
        else:
            error = 'Invalid username or password'
            return render_template('index.html' , loginform = loginform , signupform = signupform , error = error )

@app.route('/register', methods=['GET', 'POST'])
def register():
    print('register run')
    loginform = LoginForm()
    signupform = SignupForm()
    error = ''
    msg = False
    if signupform.signup.data and signupform.validate_on_submit():
        if signupform.check_email_and_username():
            print ('signup details ok')
            return redirect(url_for('home'))
    return render_template('index.html' , loginform = loginform , signupform = signupform , error = error )



if __name__ == '__main__':
    app.run(debug=True)