from os import getenv
from typing import List, Optional

from databases import Database
from fastapi import FastAPI

from app.database import connection
from app.model import models
from app.resource import item, user

app = FastAPI(title="Crud usando FastAPI - Async DB", debug=True)
db = Database(url=getenv("DATABASE_URI", ""))
models.init_app()
connection.init_app(app=app, db=db)
user.init_app(app=app, db=db)
item.init_app(app=app, db=db)
