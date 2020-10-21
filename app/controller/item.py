"""
Modulo de controller para manipular itens no banco de dados.
"""

from typing import List, Mapping

from databases import Database
from fastapi import HTTPException

from app.model.models import item
from app.schema.input import ItemSchemaBaseIn


async def inserir_item(db: Database, model: ItemSchemaBaseIn) -> dict:
    values = model.dict()
    query = item.insert().values(values)
    id = await db.execute(query=query)
    return {"id": id, **values}


async def selecionar_item(
    db: Database, user_id: int, item_id: int = None
) -> List[Mapping]:
    query = (
        item.select((item.c.usuario_id_fk == user_id) & (item.c.id == item_id))
        if item_id
        else item.select(item.c.usuario_id_fk == user_id)
    )
    result = await db.fetch_all(query=query)
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"O usuário de id: {user_id} não tem nenhum item válido.",
        )
    return result


async def atualizar_item(
    model: ItemSchemaBaseIn, db: Database, user_id: int, item_id: int
) -> dict:
    await selecionar_item(db=db, user_id=user_id, item_id=item_id)
    values = model.dict(exclude_none=True, exclude={"data_de_criacao"})
    update = (
        item.update()
        .where((item.c.usuario_id_fk == user_id) & (item.c.id == item_id))
        .values(values)
    )
    await db.execute(query=update)
    return {"id": item_id, **values}


async def deletar_item(
    db: Database,
    user_id: int,
    item_id: int = None,
    detele_by_user: bool = False,
) -> None:
    if not detele_by_user:
        await selecionar_item(db=db, user_id=user_id, item_id=item_id)
    query = (
        item.delete().where(
            (item.c.id == item_id) & (item.c.usuario_id_fk == user_id)
        )
        if item_id
        else item.delete().where(item.c.usuario_id_fk == user_id)
    )
    return await db.execute(query=query)
