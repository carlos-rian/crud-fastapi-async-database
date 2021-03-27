from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator


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

    @validator("data_de_criacao", pre=True)
    def data_de_criacao_validate(cls, data_de_criacao):
        return f"{data_de_criacao}".replace("Z", "")

    @validator("data_de_atualizacao", pre=True)
    def data_de_atualizacao_validate(cls, data_de_atualizacao):
        return f"{data_de_atualizacao}".replace("Z", "")


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

    @validator("data_de_criacao", pre=True)
    def data_de_criacao_validate(cls, data_de_criacao):
        return f"{data_de_criacao}".replace("Z", "")

    @validator("data_de_atualizacao", pre=True)
    def data_de_atualizacao_validate(cls, data_de_atualizacao):
        return f"{data_de_atualizacao}".replace("Z", "")