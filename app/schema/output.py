from .input import UsuarioSchemaIn, ItemSchemaIn
from typing import List, Optional


class ItemSchemaOut(ItemSchemaIn):
    id: int


class UsuarioSchemaOut(UsuarioSchemaIn):
    id: int
    itens: List[Optional[ItemSchemaOut]]

