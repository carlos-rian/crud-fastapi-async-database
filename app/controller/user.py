from fastapi import HTTPException
from databases import Database
from app.model.models import usuario
from app.schema.input import UsuarioSchemaBaseIn


async def inserir_usuario(db: Database, model: UsuarioSchemaBaseIn):
    values = model.dict(exclude={"itens"}, exclude_none=True, exclude_unset=True)
    query = usuario.insert().values(values)
    id = await db.execute(query=query)

    return {"id": id, **values}


async def selecionar_usuario(db: Database, id: int = None):
    query = usuario.select(usuario.c.id == id).first() if id else usuario.select()
    result = await db.fetch_all(query=query)
    if not result:
        raise HTTPException(status_code=404, detail="usuário não encontrado")

    return result


async def atualizar_usuario(model: UsuarioSchemaBaseIn, db: Database, id: int):
    result = await selecionar_usuario(db=db, id=id)
    if not result:
        raise HTTPException(status_code=404, detail="usuário não encontrado")

    values = model.dict(exclude={"itens"}, exclude_none=True, exclude_unset=True)
    update = usuario.update().where(usuario.c.id == id).values(values)
    await db.execute(query=update)

    return {"id": id, **values}


async def deletar_usuario(db: Database, id: int):
    result = await selecionar_usuario(db=db, id=id)
    if not result:
        raise HTTPException(status_code=404, detail="usuário não encontrado")

    query = usuario.delete().where(usuario.c.id == id)
    return await db.execute(query=query)
