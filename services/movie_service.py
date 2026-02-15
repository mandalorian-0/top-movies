from sqlalchemy.orm import Session
from models.movie import Movie

def get_all_movies(db: Session) -> list[Movie]:
    return db.query(Movie).all()

def get_movie_by_id(db: Session, movie_id: int) -> Movie | None :
    return db.query(Movie).filter(Movie.id == movie_id).first()

def add_movie(db: Session, movie):
    new_movie = Movie(title=movie.get("title"), img_url=movie.get("img_url"), year=movie.get("year"), description=movie.get("description"))
    
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie.id

def update_movie(db: Session, movie_id: int, movie_data: dict | None) -> Movie | None:
    movie_to_update = get_movie_by_id(db, movie_id)

    if not movie_to_update:
        return None

    movie_to_update.rating = movie_data["rating"]
    movie_to_update.review = movie_data["review"]

    db.commit()
    db.refresh(movie_to_update)
    # return movie

def delete_movie(db: Session, movie_id: int):
    movie_to_delete = get_movie_by_id(db, movie_id)

    if not movie_to_delete:
        return False

    db.delete(movie_to_delete)
    db.commit()
    return True