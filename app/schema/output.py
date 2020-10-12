from .input import ItemSchemaIn, UsuarioSchemaBaseIn
from typing import List, Optional


class ItemSchemaOut(ItemSchemaIn):
    id: int


class UsuarioSchemaBaseOut(UsuarioSchemaBaseIn):
    id: int


class UsuarioSchemaOut(UsuarioSchemaBaseOut):
    itens: List[Optional[ItemSchemaOut]]

