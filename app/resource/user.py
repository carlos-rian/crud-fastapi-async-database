from typing import List, Dict
from fastapi import FastAPI
from databases import Database
from app.error import errors
from app.schema.input import UsuarioSchemaBaseIn as usbi
from app.schema.output import UsuarioSchemaBaseOut as usbo, RespostaDeDelete as rdd
from app.controller import inserir_usuario, selecionar_usuario, atualizar_usuario, deletar_usuario


def init_app(app: FastAPI, db=Database) -> FastAPI:
    tag = ["usuário"]
    err_user = errors.usuario

    @app.post("/usuario", response_model=usbo, tags=tag, status_code=201)
    async def criar_usuario(usuario: usbi):
        result = await inserir_usuario(db=db, model=usuario)
        return result

    @app.get("/usuario", response_model=List[usbo], tags=tag, responses=err_user)
    async def pegar_todos_usuarios():
        result = await selecionar_usuario(db=db)
        return result

    @app.get("/usuario/{user_id}", response_model=usbo, tags=tag, responses=err_user)
    async def pegar_usuario(user_id: int):
        result = await selecionar_usuario(db=db, user_id=user_id)
        return result[0]

    @app.put("/usuario/{user_id}", response_model=usbo, tags=tag, responses=err_user)
    async def modificar_usuario(user_id: int, usuario: usbi):
        result = await atualizar_usuario(db=db, model=usuario, user_id=user_id)
        return result

    @app.delete("/usuario/{user_id}", response_model=rdd, tags=tag, responses=err_user)
    async def apagar_usuario(user_id: int):
        await deletar_usuario(db=db, user_id=user_id)
        return {"message": "Usuário removido com sucesso."}

    return app
