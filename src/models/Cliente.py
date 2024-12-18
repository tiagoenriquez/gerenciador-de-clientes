class Cliente:
    def __init__(self, nome: str, sobrenome: str, email: str, cpf: str, id = 0):
        self._nome = nome
        self._sobrenome = sobrenome
        self._email = email
        self._cpf = cpf
        self._id = id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def sobrenome(self):
        return self._sobrenome
    
    @property
    def email(self):
        return self._email
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def id(self):
        return self._id