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
    register_user = User(email=signupform.email.data,
                    username=signupform.username.data,
                    password=signupform.password.data)
    db.session.add(register_user)
    try:
        db.session.commit()
        msg = 'register complete'
    except:
        db.session.rollback()
        error = 'register failed'
        if not register_user.check_if_username_free() :
            error += '<br> username already exists'
        if not register_user.check_if_email_free() :
            error += '<br> email already exists'

    loginform.reset()
    signupform.reset()
    return render_template('index.html' , loginform = loginform , signupform = signupform , error = error , msg = msg )