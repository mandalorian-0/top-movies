# from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Column
from sqlalchemy.ext.declarative import declarative_base

from core.base import Base

class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String(250), unique=True, nullable=False)
    year: Mapped[int] = Column(Integer, nullable=False)
    description: Mapped[str] = Column(String(250))
    rating: Mapped[float] 
    ranking: Mapped[int] = Column(Integer, nullable=False)
    review: Mapped[str] = Column(String(250), nullable=False)
    img_url: Mapped[str] = Column(String(250), nullable=False)
