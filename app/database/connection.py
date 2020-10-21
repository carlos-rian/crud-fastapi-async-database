from os import getenv

from databases import Database
from fastapi import FastAPI


def init_app(app: FastAPI, db: Database) -> FastAPI:
    """inicializar eventos de start e stop da aplicação.

    Args:
        app (FastAPI): informe o app previamente instânciado.
        db: (Database):  informe a instância do database.
    Returns:
        FastAPI: retorna um app modificado.
    """

    @app.on_event("startup")
    async def startup():
        """
        Essa função irá conectar ao banco quando a aplicação iniciar.
        """
        await db.connect()

    @app.on_event("shutdown")
    async def shutdown():
        """
        Essa função irá deconectar do banco quando a aplicação parar.
        """
        await db.disconnect()

    return app

