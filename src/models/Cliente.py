class Cliente:
    def __init__(self, nome: str, sobrenome: str, email: str, cpf: str, id = 0):
        self._nome = nome
        self._sobrenome = sobrenome
        self._email = email
        self.cpf = cpf
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
    def id(self):
        return self._id
    
    def data_for_insertion(self):
        return [self._nome, self._sobrenome, self._email, self._cpf]
    
    def data_for_update(self):
        return [self._nome, self._sobrenome, self._email, self._cpf, self._id]