from os import getenv
from typing import List, Optional
from fastapi import FastAPI
from databases import Database

from app.model import models
from app.database import connection
from app.resource import item
from app.resource import user


app = FastAPI(title="Crud usando FastAPI - Async DB")
db = Database(url=getenv("DATABASE_URI"))
models.init_app()
connection.init_app(app=app, db=db)
user.init_app(app=app, db=db)
item.init_app(app=app, db=db)

