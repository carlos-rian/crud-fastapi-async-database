# CRUD FastAPI Com Database Async
Crud com FastAPI, SqlAlchemy e Databases.

## Descrição

Esse é um exemplo simples de API assincrona com FastAPI onde pode-se criar, ler, atualizar e deletar os dados de um banco de dados.
Basicamente esse projeto tem duas tabelas, sendo essas a de usuário e a de produtos.
Um relacionamento de 1-N, onde a tabela de produtos recebe o id do usuário.

## Depências

- docker
- docker-compose

## Como instânciar o projeto?

1 - Faça o clone do repo.
```sh
git clone https://github.com/carlos-rian/crud-fastapi-async-database.git
```

2 - Execute o comando docker abaixo para criar os containers.
```sh
docker-compose up --build -d
```

3 - Verificar os containers ativos.
```sh
docker ps
```

##