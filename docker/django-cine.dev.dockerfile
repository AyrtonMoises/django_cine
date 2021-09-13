FROM python:3.8-alpine

# Cria usuario, pasta e define como proprietario
RUN adduser -D user-app \
    && mkdir /app \
    && chown user-app: /app

# Installing client libraries and any other package you need
RUN apk update && apk add libpq

# Installing build dependencies
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev bash

# Installing and build python module
RUN pip install psycopg2

# Delete build dependencies
RUN apk del .build-deps

# Copia os arquivos do projeto para o diretorio do app
COPY --chown=user-app app/ /app/

# Definindo o diretorio onde o CMD será executado e copiando o arquivo de requerimentos
WORKDIR /app

# Seta variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

# Instalando os requerimentos com o PIP
RUN pip install -r requirements.txt

# Altera permissao para ser executavel
RUN chmod +x entrypoint.sh

# Roda comandos iniciais do app
ENTRYPOINT ["./entrypoint.sh"]