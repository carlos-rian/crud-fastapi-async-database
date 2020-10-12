from os import getenv
from typing import List, Optional
from fastapi import FastAPI
from databases import Database
from app.schema.input import UsuarioSchemaIn, UsuarioSchemaBaseIn
from app.schema.output import UsuarioSchemaOut, UsuarioSchemaBaseOut
from app.controller import (
    tratar_insert,
    pegar_usuario_e_itens,
    deletar_usuario_e_item,
    atualiza_usuario,
)
from app.database import init_db
from app.model import init_table


app = FastAPI(title="Crud usando FastAPI - Async DB")
db = Database(url=getenv("DATABASE_URI"))
init_table()
init_db(app=app, db=db)


@app.post("/usuario/", response_model=UsuarioSchemaOut, tags=["usuário"], status_code=201)
async def criar_usuario(usuario: UsuarioSchemaIn):
    result = await tratar_insert(db=db, model=usuario)
    return result


@app.get("/usuario/{id}/", response_model=UsuarioSchemaOut, tags=["usuário"])
async def pegar_usuario(id: int):
    result = await pegar_usuario_e_itens(db=db, id=id)
    return result[0]


@app.get("/usuario/", response_model=List[UsuarioSchemaOut], tags=["usuário"])
async def pegar_lista_usuarios():
    result = await pegar_usuario_e_itens(db=db)
    return result


@app.patch("/usuario/{id}/", response_model=UsuarioSchemaBaseOut, tags=["usuário"])
async def atualizar_usuario(id: int, usuario: UsuarioSchemaBaseIn):
    result = await atualiza_usuario(db=db, model=usuario, id=id)
    return result


@app.delete("/usuario/{id}/", response_model=UsuarioSchemaOut, tags=["usuário"])
async def deletar_usuario(id: int):
    result = await deletar_usuario_e_item(db=db, id=id)
    return result
