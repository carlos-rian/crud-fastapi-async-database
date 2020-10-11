from os import getenv
from sqlalchemy import create_engine
from .models import metadata


def init_table():
    DATABASE_URI = getenv("DATABASE_URI")
    engine = create_engine(DATABASE_URI, echo=True)
    metadata.create_all(bind=engine)
