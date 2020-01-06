from blog import app,db
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user, current_user
from blog.forms import LoginForm , SignupForm, AddPost
from blog.models import User , Post

@app.route('/', methods=['GET', 'POST'])
def index():
    loginform = LoginForm()
    signupform = SignupForm()
    error = []
    msg = ''
    if loginform.login.data and loginform.validate_on_submit():
        print ("login")
        logged_in_user = User.query.filter_by(username=loginform.username.data).first()
        if ( logged_in_user is not None and logged_in_user.check_password(loginform.password.data) ) :
            print (logged_in_user)
            to_remember = loginform.remember.data
            login_user(logged_in_user , remember = to_remember)
            return redirect(url_for('home'))
        else:
            error.append('Invalid username or password')
            return render_template('index.html' , loginform = loginform , signupform = signupform , error = error )

    if signupform.signup.data and signupform.validate_on_submit():
        print('signup')
        register_user = User(email=signupform.email.data,
                    username=signupform.username.data,
                    password=signupform.password.data)
        db.session.add(register_user)
        try:
            db.session.commit()
            msg = 'register complete'
        except:
            db.session.rollback()
            error.append('register failed')
            if not register_user.check_if_username_free() :
                error.append('username already exists')
            if not register_user.check_if_email_free() :
                error.append('email already exists')

    loginform.reset()
    signupform.reset()
    return render_template('index.html' , loginform = loginform , signupform = signupform , error = error , msg=msg )


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    msg = []
    addpost_form= AddPost()
    if addpost_form.addpost.data:
        new_post = Post(current_user.username , addpost_form.data['post'])
        db.session.add(new_post)
        db.session.commit()
        msg.append('Post added')
        print ('added a post')
        addpost_form.data['post'] =""
    
    
    return render_template('home.html' , addpost_form=addpost_form , msg=msg)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect (url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user, posts=posts)