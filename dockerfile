FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get install curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /app

ADD /app/. /app

RUN pip install --upgrade pip

RUN poetry install