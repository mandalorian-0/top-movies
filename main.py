import requests

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

from db.__init__ import SessionLocal, create_tables
from services.movie_service import get_all_movies, update_movie
from form.update import UpdateForm

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
    movies = get_all_movies(db)

    return render_template("index.html", movies=movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = UpdateForm()
    db = next(get_db())
    movie_id = request.args.get('id')

    if form.validate_on_submit():
        # new_rating = form.data["rating"]
        # new_review =form.data["review"]

        try:
            update_movie(db, movie_id, form.data)
            return redirect(url_for("home"))
        except Exception as e:
            print(e)

        
    return render_template("edit.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
