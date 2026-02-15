import requests

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from db.__init__ import SessionLocal, create_tables
from services.movie_service import get_all_users

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

def init_app():
    create_tables()

init_app()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.route("/")
def home():
    db = next(get_db())
    movies = get_all_users(db)

    return render_template("index.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
