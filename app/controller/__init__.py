from fastapi import HTTPException
from sqlalchemy import Table
from databases import Database
from app.model.models import item, usuario
from app.schema.input import UsuarioSchemaIn


async def inserir_usuario_e_itens(table: Table, values: dict, db: Database):
    query = table.insert().values(values)
    id = await db.execute(query=query)
    return {"id": id, **values}


async def tratar_insert(db: Database, model: UsuarioSchemaIn):
    user_dict = model.dict(exclude={"itens"})
    result_usuario = await inserir_usuario_e_itens(table=usuario, values=user_dict, db=db)
    itens = []
    for item_model in model.itens:
        item_dict = {**item_model.dict(), "usuario_id_fk": result_usuario["id"]}
        item_com_id = await inserir_usuario_e_itens(table=item, values=item_dict, db=db)
        itens.append(item_com_id)
    return {**result_usuario, "itens": itens}


async def pegar_itens_do_usuario(db: Database, id: int):
    query = item.select(item.c.usuario_id_fk == id)
    result = await db.fetch_all(query=query)
    return result


async def pegar_usuario_e_itens(db: Database, id: int = None):
    if id:
        query = usuario.select(usuario.c.id == id)
    else:
        query = usuario.select()

    result_usuario = await db.fetch_all(query=query)
    if not result_usuario:
        raise HTTPException(status_code=404, detail="usuário não encontrado",)

    for index, data in enumerate(result_usuario):
        data = dict(data)
        itens = await pegar_itens_do_usuario(db=db, id=data["id"])
        result_usuario[index] = {**data, "itens": itens}

    return result_usuario


async def atualizar_usuario(table: Table, values: dict, db: Database, id: int = None):
    query = table.select(table.c.id == id)
    result = await db.fetch_all(query=query)
    if not result:
        raise HTTPException(status_code=404, detail="usuário não encontrado")

    query = table.update().where(table.c.id == id).values(values)
    await db.execute(query=query)
    return {**values, "id": id}


async def deletar_usuario(table: Table, db: Database, id: int = None):
    query = table.select().where(table.c.id == id)
    result = await db.fetch_all(query=query)
    if not result:
        raise HTTPException(status_code=404, detail="usuário não encontrado")

    await table.delete().where(table.c.id == id)
    return result
