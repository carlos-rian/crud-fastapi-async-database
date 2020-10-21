from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional, List


class ItemSchemaBaseIn(BaseModel):
    """
    Modelo de entrada de novos Itens.
    Essa classe será responsável por validar os dados de entradas.
    A validação é feita por meio da lib pydantic.
    """

    item: str
    preco: float
    quantidade: int
    descricao: Optional[str] = None
    usuario_id_fk: Optional[int] = None
    data_de_criacao: datetime = Field(default_factory=datetime.now)
    data_de_atualizacao: datetime = Field(default_factory=datetime.now)


class UsuarioSchemaBaseIn(BaseModel):
    """
    Modelo de entrada de novos Usuários.
    Essa classe será responsável por validar os dados de entradas.
    A validação é feita por meio da lib pydantic.
    """

    nome: str
    sobrenome: str
    funcionario: Optional[bool] = False
    data_de_nascimento: Optional[date] = None
    data_de_criacao: datetime = Field(default_factory=datetime.now)
    data_de_atualizacao: datetime = Field(default_factory=datetime.now)

