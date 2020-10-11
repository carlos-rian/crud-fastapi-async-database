from os import getenv
from databases import Database
from fastapi import FastAPI


def init_db(app: FastAPI, db: Database) -> FastAPI:
    """inicializar eventos de start e stop da aplicação.

    Args:
        app (FastAPI): informe o app previamente instânciado.
        db: (Database):  informe a instância do database.
    Returns:
        FastAPI: retorna um app modificado.
    """

    @app.on_event("startup")
    async def startup():
        await db.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await db.disconnect()

    return app

