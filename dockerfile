FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/app/

ADD /app/. /app/app/

COPY requirements.txt /app/app/

RUN pip install --upgrade --user --no-warn-script-location pip 

RUN pip install -r requirements.txt 
