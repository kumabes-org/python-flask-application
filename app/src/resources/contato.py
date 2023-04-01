from flask_restful import Resource, reqparse
from models.contato import ContatoModel


contatos = [
            {
                "codigo": 1,
                "nome": "Beltrano",
                "telefone": "(37) 99999-9999",
                "data_nascimento": "1985-06-03"
            },
                        {
                "codigo": 2,
                "nome": "Fulano",
                "telefone": "(11) 99999-9999",
                "data_nascimento": "1994-01-29"
            },
            {
                "codigo": 3,
                "nome": "Sicrano",
                "telefone": "(21) 99999-9999",
                "data_nascimento": "1995-08-15"
            }
        ]


class Contatos(Resource):
    def get(self):
        return contatos

class Contato(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('telefone')
    argumentos.add_argument('data_nascimento')
    
    def get(self, codigo):
        contato = Contato.find_contato(codigo)
        if contato:
            return contato
        return {'message': 'Contato não encontrado!'}, 404

    def post(self, codigo):
        if ContatoModel.find_contato(codigo):
            return {"message": f"Contato com o codigo \"{codigo}\" já existe!"}, 400
        dados = Contato.argumentos.parse_args()
        objeto = ContatoModel(codigo, **dados)
        objeto.save_contato()
        return objeto.json(), 201

    def put(self, codigo):
        dados = Contato.argumentos.parse_args()
        objeto = ContatoModel(codigo, **dados)
        novo_contato = objeto.json()
        contato = Contato.find_contato(codigo)
        if contato:            
            contato.update(novo_contato)
            return novo_contato, 200
        contatos.append(novo_contato)
        return novo_contato, 201

    def delete(self, codigo):
        global contatos
        contatos = [contato for contato in contatos if contato['codigo'] != codigo]
        return {'message': 'Contato deletado!'}, 204