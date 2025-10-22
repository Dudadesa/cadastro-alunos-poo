class Aluno:
    def __init__(self, id=None, nome="", cpf="", data_nascimento="", status="ativo"):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.status = status

    def __repr__(self):
        return f"Aluno(id={self.id}, nome='{self.nome}', cpf='{self.cpf}', data_nascimento='{self.data_nascimento}', status='{self.status}')"
