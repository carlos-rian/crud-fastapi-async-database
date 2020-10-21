from pydantic import BaseModel


class DefaultError(BaseModel):
    """
    Essa classe faz o mapeamento do erro possivel, 
    caso não enconte um item ou usuário.
    """

    detail: str


usuario = {
    404: {
        "description": "Erro ao consultar usuário, não existe na base.",
        "model": DefaultError,
    }
}

item = {
    404: {
        "description": (
            "Erro ao consultar item do usuário, não foi "
            "encontrado nenhum item ou o usuário não existe."
        ),
        "model": DefaultError,
    }
}
