from pydantic import BaseModel


class DefaultError(BaseModel):
    detail: str


usuario = {
    404: {
        "description": "Erro ao consultar usuário, o mesmo não existe na base.",
        "model": DefaultError,
    }
}

item = {
    404: {
        "description": "Erro ao consultar item do usuário, não foi encontrado nenhum item.",
        "model": DefaultError,
    }
}
