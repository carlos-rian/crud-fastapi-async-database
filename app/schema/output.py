from .input import ItemSchemaBaseIn, UsuarioSchemaBaseIn
from typing import List, Optional


class ItemSchemaOut(ItemSchemaBaseIn):
    id: int


class UsuarioSchemaBaseOut(UsuarioSchemaBaseIn):
    id: int


class UsuarioSchemaOut(UsuarioSchemaBaseOut):
    itens: List[Optional[ItemSchemaOut]]

