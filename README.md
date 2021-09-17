### Docker com Django, Postgres, Gunicorn e Nginx


## Desenvolvimento

Usando o servidor de desenvolvimento do Django.

1. Renomear o arquivo da pasta *.envs*: *.django.dev-sample* para *.django.dev*.
1. Atualize as variáveis de ambiente em *docker-compose.dev.yml* e *.django.dev*.
1. Contruir as imagens e rodar os contâiners :
2. 
    ```sh
    $ docker-compose -f docker-compose.dev.yml up -d --build
    ```

    Teste em [http://0.0.0.0:8000](http://0.0.0.0:8000). A pasta "app" e montada no contâiner e as mudanças no código são feitas automaticamente.

## Produção

Usando gunicorn + nginx.

1. Renomear os arquivos da pasta *.envs*: *.django.prod-sample* para *.django.prod* e *.db.prod-sample* para *.db.prod*.
1. Construir as imagens e rodar os contâiners:

    ```sh
    $ docker-compose up -d --build
    ```

    Teste em [http://0.0.0.0:80](http://0.0.0.0:80). Não é montado. Para aplicar as mudanças, as imagens devem ser reconstruídas.