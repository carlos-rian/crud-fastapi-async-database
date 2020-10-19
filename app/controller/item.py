from databases import Database
from app.model.models import item
from app.schema.input import ItemSchemaBaseIn


async def inserir_item(db: Database, model: ItemSchemaBaseIn):
    values = model.dict(exclude={"itens"}, exclude_none=True, exclude_unset=True)
    query = item.insert().values(values)
    id = await db.execute(query=query)
    return {"id": id, **values}


async def selecionar_item(db: Database, id: int):
    query = item.select(item.c.usuario_id_fk == id)
    result = await db.fetch_all(query=query)
    return result


async def atualizar_item(model: ItemSchemaBaseIn, db: Database, id: int):
    result = await selecionar_item(db=db, id=id)
    if not result:
        raise HTTPException(status_code=404, detail="usuário não encontrado")

    values = model.dict(exclude={"itens"}, exclude_none=True, exclude_unset=True)
    update = item.update().where(item.c.id == id).values(values)
    await db.execute(query=update)

    return {"id": id, **values}


async def deletar_item(db: Database, id: int):
    result = await selecionar_item(db=db, id=id)
    if not result:
        raise HTTPException(status_code=404, detail="usuário não encontrado")

    query = item.delete().where(item.c.id == id)
    return await db.execute(query=query)
