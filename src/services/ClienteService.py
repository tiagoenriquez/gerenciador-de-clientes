from src.models.Cliente import Cliente
from src.repositories.ClienteRepository import ClienteRepository


class ClienteService:
    def _checar_email(self, email: str):
        if "@" not in email:
            raise Exception("E-mail inválido")
    
    def _checar_cpf(self, cpf: str):
        if not cpf.isnumeric():
            raise Exception("CPF inválido")
    
    def _editar_cpf(self, cpf: str):
        parte1 = cpf[0:3]
        parte2 = cpf[3:6]
        parte3 = cpf[6:9]
        parte4 = cpf[9:11]
        return f"{parte1}.{parte2}.{parte3}-{parte4}"

    def inserir(self, cliente: Cliente):
        self._checar_email(cliente.email)
        self._checar_cpf(cliente.cpf)
        cliente.cpf = self._editar_cpf(cliente.cpf)
        ClienteRepository().inserir(cliente)