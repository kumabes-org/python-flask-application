from flask import Flask
from flask_restful import Resource, Api
from resources.contato import Contatos, Contato

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/contatos_db?charset=utf8mb4&collation=utf8mb4_unicode_ci'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

# @app.before_first_request
# def cria_banco():
#     banco.create_all()

api.add_resource(Contatos, "/api/v1/contatos")
api.add_resource(Contato, "/api/v1/contatos/<int:codigo>")


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)