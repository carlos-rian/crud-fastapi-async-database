from typing import Dict, List

from app.controller import atualizar_usuario, deletar_usuario, inserir_usuario, selecionar_usuario
from app.error import errors
from app.schema.input import UsuarioSchemaBaseIn as usbi
from app.schema.output import RespostaDeDelete as rdd
from app.schema.output import UsuarioSchemaBaseOut as usbo
from databases import Database
from fastapi import FastAPI


def init_app(app: FastAPI, db=Database) -> FastAPI:
    tag = ["usuário"]
    err_user = errors.usuario

    @app.post("/usuario", response_model=usbo, tags=tag, status_code=201)
    async def criar_usuario(usuario: usbi):
        """
        Crie um novo usuário, não precisa informar as datas de criação e alteração.
        """
        result = await inserir_usuario(db=db, model=usuario)
        return result

    @app.get("/usuario", response_model=List[usbo], tags=tag, responses=err_user)
    async def pegar_todos_usuarios():
        """
        Essa função irá retornar todos os usuário cadastrados no banco.
        """
        result = await selecionar_usuario(db=db)
        return result

    @app.get("/usuario/{user_id}", response_model=usbo, tags=tag, responses=err_user)
    async def pegar_usuario(user_id: int):
        """
        Consulte um usuário por meio do ID.
        - **user_id**: informe o user_id do usuário que deseja filtrar.
        """
        result = await selecionar_usuario(db=db, user_id=user_id)
        return result[0]

    @app.put("/usuario/{user_id}", response_model=usbo, tags=tag, responses=err_user)
    async def modificar_usuario(user_id: int, usuario: usbi):
        """
        Atualize o cadastro de um usuário existe, para isso informe o id 
        e passe os dados que deseja atualizar.
        - **user_id**: informe o user_id do usuário que deseja modifica.
        """
        result = await atualizar_usuario(db=db, model=usuario, user_id=user_id)
        return result

    @app.delete("/usuario/{user_id}", response_model=rdd, tags=tag, responses=err_user)
    async def apagar_usuario(user_id: int):
        """
        Faça a remoção de um usuário previamente cadastrado.
        - **user_id**: informe o user_id do usuário que deseja excluir.
        """
        await deletar_usuario(db=db, user_id=user_id)
        return {"message": "Usuário removido com sucesso."}

    return app
