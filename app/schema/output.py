from pydantic import BaseModel
from .input import ItemSchemaBaseIn, UsuarioSchemaBaseIn
from typing import List, Optional


class RespostaDeDelete(BaseModel):
    """
    Essa classe é reponsável por implementar o modelo de mensagem de saida em caso de errors.
    """

    message: str = "Usuário ou Item não encotrado."


class ItemSchemaOut(ItemSchemaBaseIn):
    """
    Essa classe herda do schema de entrada do item e adiciona o campo id.
    """

    id: int


class UsuarioSchemaBaseOut(UsuarioSchemaBaseIn):
    """
    Essa classe herda do schema de entrada do usuário e adiciona o campo id.
    """

    id: int


class UsuarioItemSchemaOut(UsuarioSchemaBaseOut):
    """
    Essa classe herda do schema de saida do usuário e adiciona o campo itens.
    """

    itens: List[Optional[ItemSchemaOut]]

