from os import getenv
from sqlalchemy import create_engine

from sqlalchemy import (
    Table,
    String,
    Integer,
    Boolean,
    DateTime,
    Date,
    Float,
    Text,
    MetaData,
    Column,
    ForeignKeyConstraint,
)


metadata = MetaData()

usuario = Table(
    "usuarios",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nome", String(50), nullable=False),
    Column("sobrenome", String(100), nullable=False),
    Column("funcionario", Boolean, nullable=True),
    Column("data_de_nascimento", Date, nullable=True),
    Column("data_de_criacao", DateTime, nullable=False),
    Column("data_de_atualizacao", DateTime, nullable=False),
)

item = Table(
    "itens",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("item", String(100), nullable=False),
    Column("preco", Float, nullable=False),
    Column("quantidade", Integer, nullable=False),
    Column("descricao", Text, nullable=True),
    Column("usuario_id_fk", Integer, nullable=False),
    Column("data_de_criacao", DateTime, nullable=False),
    Column("data_de_atualizacao", DateTime, nullable=False),
    ForeignKeyConstraint(
        columns=["usuario_id_fk"], refcolumns=["usuarios.id"], name="fk_item_usuario_id",
    ),
)


def init_app():
    """
    Essa função irá criar as tabelas no banco de dados.
    """
    DATABASE_URI = getenv("DATABASE_URI")
    engine = create_engine(DATABASE_URI, echo=True)
    metadata.create_all(bind=engine)
