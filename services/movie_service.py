from sqlalchemy.orm import Session
from models.movie import Movie

def get_all_movies(db: Session) -> list[Movie]:
    return db.query(Movie).all()

def get_movie_by_id(db: Session, movie_id: int)-> Movie | None :
    return db.query(Movie).filter(Movie.id == movie_id).first()

def update_movie(db: Session, id: int, movie_data: dict | None) -> Movie | None:
    movie = get_movie_by_id(db, id)

    if not movie:
        return None

    movie.rating = movie_data["rating"]
    movie.review = movie_data["review"]

    db.commit()
    db.refresh(movie)
    # return movie
