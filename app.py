from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

from models import db, User, Content, WatchHistory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initialize db with the app
db.init_app(app)


# Import models after db to prevent circular import
from models import User, Content, WatchHistory

# User Authentication Routes
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Hash password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))
        flash('Login failed. Check your credentials.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

# Content Browsing and Watching Routes
@app.route('/')
@app.route('/home')
def home():
    content_list = Content.query.all()
    return render_template('home.html', content=content_list)

@app.route('/browse')
def browse():
    genre = request.args.get('genre')
    if genre:
        content_list = Content.query.filter_by(genre=genre).all()
    else:
        content_list = Content.query.all()
    return render_template('browse.html', content=content_list)

@app.route('/watch/<int:content_id>')
def watch(content_id):
    content = Content.query.get_or_404(content_id)
    if 'user_id' in session:
        user_id = session['user_id']
        watch_entry = WatchHistory(user_id=user_id, content_id=content.id)
        db.session.add(watch_entry)
        db.session.commit()
    return render_template('watch.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
