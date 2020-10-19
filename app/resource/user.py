from typing import List
from fastapi import FastAPI
from databases import Database
from app.schema.input import UsuarioSchemaBaseIn
from app.schema.output import UsuarioSchemaOut, UsuarioSchemaBaseOut
from app.controller import (
    inserir_usuario,
    selecionar_usuario,
    atualizar_usuario,
    deletar_usuario,
    deletar_item,
)


def init_app(app: FastAPI, db=Database) -> FastAPI:
    @app.post("/usuario/", response_model=UsuarioSchemaOut, tags=["usuário"], status_code=201)
    async def criar_usuario(usuario: UsuarioSchemaBaseIn):
        result = await inserir_usuario(db=db, model=usuario)
        return result

    @app.get("/usuario/{id}/", response_model=UsuarioSchemaOut, tags=["usuário"])
    async def pegar_usuario(id: int):
        result = await selecionar_usuario(db=db, id=id)
        return result

    @app.get("/usuario/", response_model=List[UsuarioSchemaOut], tags=["usuário"])
    async def pegar_todos_usuarios():
        result = await selecionar_usuario(db=db)
        return result

    @app.patch("/usuario/{id}/", response_model=UsuarioSchemaBaseOut, tags=["usuário"])
    async def modificar_usuario(id: int, usuario: UsuarioSchemaBaseIn):
        result = await atualizar_usuario(db=db, model=usuario, id=id)
        return result

    @app.delete("/usuario/{id}/", response_model=UsuarioSchemaOut, tags=["usuário"])
    async def apagar_usuario(id: int):
        await deletar_item(db=db, id=id)
        result = await deletar_usuario(db=db, id=id)
        return result

    return app
