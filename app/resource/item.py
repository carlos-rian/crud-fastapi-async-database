from typing import Optional
from fastapi import FastAPI
from databases import Database
from app.controller import (
    inserir_item,
    selecionar_usuario,
    selecionar_item,
    atualizar_item,
    deletar_item,
)
from app.schema.input import ItemSchemaBaseIn as isbi
from app.schema.output import ItemSchemaOut as iso
from app.schema.output import RespostaDeDelete as rdd
from app.schema.output import UsuarioItemSchemaOut as uso
from app.error import errors


def init_app(app: FastAPI, db: Database) -> FastAPI:
    tag = ["item"]
    err_item = errors.item

    @app.post("/usuario/{user_id}/item", response_model=iso, tags=["item"])
    async def criar_item(user_id: int, item: isbi):
        await selecionar_usuario(db=db, user_id=user_id)
        item.usuario_id_fk = user_id
        result = await inserir_item(db=db, model=item)
        return result

    @app.get("/usuario/{user_id}/item", response_model=uso, tags=tag, responses=err_item)
    async def pegar_itens(user_id: int):
        """
        - **user_id**: informe o id do usuário que deseja buscar os itens.
        """
        usuario = await selecionar_usuario(db=db, user_id=user_id)
        item = await selecionar_item(db=db, user_id=user_id)
        return {**usuario[0], "itens": item}

    @app.get("/usuario/{user_id}/item/{item_id}", response_model=uso, tags=tag, responses=err_item)
    async def pegar_item(user_id: int, item_id: int):
        usuario = await selecionar_usuario(db=db, user_id=user_id)
        item = await selecionar_item(db=db, user_id=user_id, item_id=item_id)
        return {**usuario[0], "itens": item}

    @app.put("/usuario/{user_id}/item/{item_id}", response_model=iso, tags=tag, responses=err_item)
    async def modificar_item(user_id: int, item_id: int, item: isbi):
        result = await atualizar_item(model=item, db=db, user_id=user_id, item_id=item_id)
        return result

    @app.delete("/usuario/{user_id}/item", tags=tag, response_model=rdd, responses=err_item)
    async def apagar_itens(user_id: int):
        await deletar_item(db=db, user_id=user_id)
        return {"message": f"O usuário de id: {user_id} teve todos os itens removidos com sucesso."}

    @app.delete(
        "/usuario/{user_id}/item/{item_id}", response_model=rdd, tags=tag, responses=err_item
    )
    async def apagar_item(user_id: int, item_id: int):
        await deletar_item(db=db, user_id=user_id, item_id=item_id)
        return {
            "message": f"O usuário de id: {user_id} teve o item: {item_id} removido com sucesso."
        }

    return app
