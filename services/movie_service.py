from sqlalchemy.orm import Session
from models.movie import Movie

def get_all_users(db: Session) -> list[Movie]:
    return db.query(Movie).all()