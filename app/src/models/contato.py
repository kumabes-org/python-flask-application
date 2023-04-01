from sql_alchemy import banco

class ContatoModel(banco.Model):
    __tablename__ = 'contatos'
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_collate": "utf8_unicode_ci",
        "mysql_charset": "utf8",
    }
    
    codigo = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(160,collation='utf8_unicode_ci'))
    telefone = banco.Column(banco.String(16,collation='utf8_unicode_ci'))
    data_nascimento = banco.Column(banco.String(10,collation='utf8_unicode_ci'))

    @classmethod
    def find_contato(cls, codigo):
        contato = cls.query.filter_by(codigo=codigo).first()
        if contato:
            return contato
        else:
            return None

    def __init__(self, codigo, nome, telefone, data_nascimento):
        self.codigo = codigo
        self.nome = nome
        self.telefone = telefone
        self.data_nascimento = data_nascimento

    def json(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "telefone": self.telefone,
            "data_nascimento": self.data_nascimento
        }

    def save_contato(self):    
        banco.session.add(self)
        banco.session.commit()