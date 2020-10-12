from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional, List


class ItemSchemaIn(BaseModel):
    item: str
    preco: float
    estoque: int
    descricao: Optional[str] = None
    data_de_criacao: datetime = Field(default_factory=datetime.now)
    data_de_atualizacao: datetime = Field(default_factory=datetime.now)


class UsuarioSchemaBaseIn(BaseModel):
    nome: str
    sobrenome: str
    funcionario: Optional[bool] = False
    data_de_nascimento: Optional[date] = None
    data_de_criacao: datetime = Field(default_factory=datetime.now)
    data_de_atualizacao: datetime = Field(default_factory=datetime.now)


class UsuarioSchemaIn(UsuarioSchemaBaseIn):
    itens: List[Optional[ItemSchemaIn]] = None

