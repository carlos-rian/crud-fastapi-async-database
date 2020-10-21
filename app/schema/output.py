from pydantic import BaseModel
from .input import ItemSchemaBaseIn, UsuarioSchemaBaseIn
from typing import List, Optional


class RespostaDeDelete(BaseModel):
    message: str = "Usuário ou Item não encotrado."


class ItemSchemaOut(ItemSchemaBaseIn):
    id: int


class UsuarioSchemaBaseOut(UsuarioSchemaBaseIn):
    id: int


class UsuarioItemSchemaOut(UsuarioSchemaBaseOut):
    itens: List[Optional[ItemSchemaOut]]

