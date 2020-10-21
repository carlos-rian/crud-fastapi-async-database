from databases import Database
from fastapi import HTTPException

from app.model.models import usuario
from app.schema.input import UsuarioSchemaBaseIn

from .item import deletar_item


async def inserir_usuario(db: Database, model: UsuarioSchemaBaseIn):
    values = model.dict()
    query = usuario.insert().values(values)
    id = await db.execute(query=query)
    return {"id": id, **values}


async def selecionar_usuario(db: Database, user_id: int = None):
    query = (
        usuario.select(usuario.c.id == user_id)
        if user_id
        else usuario.select()
    )
    result = await db.fetch_all(query=query)
    if not result:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return result


async def atualizar_usuario(
    model: UsuarioSchemaBaseIn, db: Database, user_id: int
):
    await selecionar_usuario(db=db, user_id=user_id)
    values = model.dict(exclude_none=True, exclude={"data_de_criacao"})
    update = usuario.update().where(usuario.c.id == user_id).values(values)
    await db.execute(query=update)
    return {"id": user_id, **values}


async def deletar_usuario(db: Database, user_id: int):
    await selecionar_usuario(db=db, user_id=user_id)
    await deletar_item(db=db, user_id=user_id, detele_by_user=True)
    query = usuario.delete().where(usuario.c.id == user_id)
    return await db.execute(query=query)
