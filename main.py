from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

from db.__init__ import SessionLocal, create_tables
from services.movie_service import get_all_movies, update_movie, delete_movie, add_movie
from form.update import UpdateForm
from form.add_movie import AddMovieForm
from api import api

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

@app.route("/movies")
def home():
    db = next(get_db())
    movies = get_all_movies(db)

    if request.args:
        try:
            movie_id = request.args.get("id")
            delete_movie(db, movie_id)
            return redirect(url_for("home"))
        except Exception as e:
            print(e)
    return render_template("index.html", movies=movies)

@app.route("/movies/edit", methods=["GET", "POST"])
def edit():
    form = UpdateForm()
    db = next(get_db())
    movie_id = request.args.get('id')

    if form.validate_on_submit():

        try:
            update_movie(db, movie_id, form.data)
            return redirect(url_for("home"))
        except Exception as e:
            print(e)
        
    return render_template("edit.html", form=form)

@app.route("/movies/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    pre = "https://image.tmdb.org/t/p/original"
    db = next(get_db())

    if request.args:
        movie_id = request.args.get("id")
        movie_detail = api.get_movie_details(movie_id)

        # add new movie based on the fetched movie
        new_movie: dict[str, str] = {
            "title": movie_detail.get("title"),
            "img_url": f"{pre}{movie_detail.get("poster_path")}",
            "year": movie_detail.get("release_date"),
            "description": movie_detail.get("overview")
        }
        new_movie_id = add_movie(db, new_movie)
        return redirect(url_for("edit", id=new_movie_id))

    if form.validate_on_submit():
        movie_title = form.data.get('title')
        movies = api.movie_title_lookup(movie_title)

        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
