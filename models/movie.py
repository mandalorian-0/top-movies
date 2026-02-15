from sqlalchemy.orm import Mapped
from sqlalchemy import Integer, String, Float, Column
from sqlalchemy.ext.declarative import declarative_base

from db.__init__ import Base

class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String(250), unique=True, nullable=False)
    year: Mapped[int] = Column(Integer, nullable=False)
    description: Mapped[str] = Column(String(250))
    rating: Mapped[float] = Column(Float, default=0.0)
    ranking: Mapped[int] = Column(Integer, default=0)
    review: Mapped[str] = Column(String(250), nullable=False, default="")
    img_url: Mapped[str] = Column(String(250), nullable=False)
