import os
from flask import Flask, render_template, flash, request, url_for, redirect
from models import Author, Message, db

#Need to run the following command in the terminal: db_init.py
app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25598'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Connect to existing database.
db.init_app(app)

@app.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        authorid = request.form['authorid']
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        elif not authorid:
            flash('Author is required!')
        else:
            try:
                m = Message(title, content)
                m.author_id = authorid
                db.session.add(m)
                db.session.commit()

            except ValueError as e:
                flash(str(e))
                return render_template('create.html')
            return redirect(url_for('index'))

    return render_template('create.html', authors=Author.query.all())