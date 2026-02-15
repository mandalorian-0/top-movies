from sqlalchemy.orm import sessionmaker
from core.base import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)