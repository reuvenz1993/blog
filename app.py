from blog import app,db
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user
from blog.forms import LoginForm , SignupForm 
from blog.models import User


@app.route('/', methods=['GET', 'POST'])
def index():
    loginform = LoginForm()
    signupform = SignupForm()
    if loginform.validate_on_submit():
        login_user = User.query.filter_by(username=loginform.email.data).first()
        if login_user.check_password(loginform.password.data) and login_user is not None:
            login_user(login_user)
            redirect(url_for('home'))

    if signupform.validate_on_submit():
        signup_user = User(email=signupform.email.data,
        username=signupform.username.data,
        password=signupform.password.data)
        db.session.add(signup_user)
        db.session.commit()

    return render_template('index.html' , loginform = loginform , signupform = signupform )



if __name__ == '__main__':
    app.run(debug=True)
