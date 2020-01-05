from blog import app,db
from flask import render_template, redirect, request, url_for, flash,abort


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
