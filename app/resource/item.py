from fastapi import FastAPI
from databases import Database
from app.controller import inserir_item, selecionar_usuario
from app.schema.input import ItemSchemaBaseIn
from app.schema.output import ItemSchemaOut


def init_app(app: FastAPI, db: Database) -> FastAPI:
    @app.post("/usuario/{user_id}/item/", response_model=ItemSchemaOut, tags=["item"])
    async def criar_item(user_id: int, item: ItemSchemaBaseIn):
        await selecionar_usuario(db=db, id=user_id)
        item.usuario_id_fk = user_id
        result = await inserir_item(db=db, model=item)
        return result

