# python-flask-application

## Python e Pip instalados
```
python -V && pip -V
Python 3.10.6
pip 22.0.2
```

## Virtual Env
```
pip install virtualenv --user
virtualenv venv --python=python3.10
source ./venv/bin/activate
## para desenvolvimento
pip install -r requirements.txt
## para testes
pip install -r requirements_tests.txt
## desativando ambiente virtual
deactivate
```

- Create:
```
curl -X POST -H 'Content-Type: application/json' http://localhost:5000/api/v1/contatos/4 -d '{"nome": "Rodrigo", "telefone": "(11) 91234-5678", "data_nascimento": "1986-03-08"}'
```

- Retrieve - Instância
```
curl -X GET http://localhost:5000/api/v1/contatos/2
```

- Update
```
curl -X PUT -H 'Content-Type: application/json' http://localhost:5000/api/v1/contatos/4 -d '{"nome": "Rodrigo", "telefone": "(11) 91234-5678", "data_nascimento": "1986-03-08"}'

curl -X PUT -H 'Content-Type: application/json' http://localhost:5000/api/v1/contatos/4 -d '{"nome": "Rodrigo T.K", "telefone": "(11) 91234-5678", "data_nascimento": "1986-03-08"}'
```

- Delete
```
curl -X DELETE http://localhost:5000/api/v1/contatos/4
```

- List - Coleção
```
curl -X GET http://localhost:5000/api/v1/contatos
[
    {
        "nome": "Fulano",
        "telefone": "(11) 99999-9999",
        "data_nascimento": "1964-04-05"
    },
    {
        "nome": "Beltrano",
        "telefone": "(11) 88888-8888",
        "data_nascimento": "1966-08-13"
    }
]
```