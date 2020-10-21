from databases import Database
from fastapi import FastAPI

from app.controller import (atualizar_item, deletar_item, inserir_item,
                            selecionar_item, selecionar_usuario)
from app.error import errors
from app.schema.input import ItemSchemaBaseIn
from app.schema.output import (ItemSchemaOut, RespostaDeDelete,
                               UsuarioItemSchemaOut)


def init_app(app: FastAPI, db: Database) -> FastAPI:
    tag = ["item"]
    err_item = errors.item

    @app.post(
        "/usuario/{user_id}/item", response_model=ItemSchemaOut, tags=["item"]
    )
    async def criar_item(user_id: int, item: ItemSchemaBaseIn):
        """ 
        Crie um novo item para um usuário.
        - **user_id**: informe o user_id do usuário.
        """
        await selecionar_usuario(db=db, user_id=user_id)
        item.usuario_id_fk = user_id
        result = await inserir_item(db=db, model=item)
        return result

    @app.get(
        "/usuario/{user_id}/item",
        response_model=UsuarioItemSchemaOut,
        tags=tag,
        responses=err_item,
    )
    async def pegar_itens(user_id: int):
        """
        Faça um filtro de todos os itens de um usuário por meio do id.
        - **user_id**: informe o id do usuário que deseja buscar os itens.
        """
        usuario = await selecionar_usuario(db=db, user_id=user_id)
        item = await selecionar_item(db=db, user_id=user_id)
        return {**usuario[0], "itens": item}

    @app.get(
        "/usuario/{user_id}/item/{item_id}",
        response_model=UsuarioItemSchemaOut,
        tags=tag,
        responses=err_item,
    )
    async def pegar_item(user_id: int, item_id: int):
        """
        Faça um filtro por um item especifico de um usuário.
        - **user_id**: informe o id do usuário que deseja buscar os itens.
        - **item_id**: informe o id do item que deseja buscar.
        """
        usuario = await selecionar_usuario(db=db, user_id=user_id)
        item = await selecionar_item(db=db, user_id=user_id, item_id=item_id)
        return {**usuario[0], "itens": item}

    @app.put(
        "/usuario/{user_id}/item/{item_id}",
        response_model=ItemSchemaOut,
        tags=tag,
        responses=err_item,
    )
    async def modificar_item(
        user_id: int, item_id: int, item: ItemSchemaBaseIn
    ):
        """
        Modifique um item especifico de un usuário por meio do id do item.
        - **user_id**: informe o id do usuário que deseja alterar o item.
        - **item_id**: informe o id do item que deseja alterar.
        """
        result = await atualizar_item(
            model=item, db=db, user_id=user_id, item_id=item_id
        )
        return result

    @app.delete(
        "/usuario/{user_id}/item",
        tags=tag,
        response_model=RespostaDeDelete,
        responses=err_item,
    )
    async def apagar_itens(user_id: int):
        """
        Você pode apagar todos os items de um usuário, informando o id dele.
        - **user_id**: informe o id do usuário, para deletar todos os itens.
        """
        await deletar_item(db=db, user_id=user_id)
        return {
            "message": (
                f"O usuário de id: {user_id} "
                "teve todos os itens removidos com sucesso."
            )
        }

    @app.delete(
        "/usuario/{user_id}/item/{item_id}",
        response_model=RespostaDeDelete,
        tags=tag,
        responses=err_item,
    )
    async def apagar_item(user_id: int, item_id: int):
        """
        Você também pode apagar apenas um item do usuário.
        - **user_id**: informe o id do usuário.
        - **item_id**: informe o id do item que deseja deletar..
        """
        await deletar_item(db=db, user_id=user_id, item_id=item_id)
        return {
            "message": (
                f"O usuário de id: {user_id} teve "
                f"o item: {item_id} removido com sucesso."
            )
        }

    return app
