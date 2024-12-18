from src.connections.DatabaseConnection import con
from src.models.Cliente import Cliente


class ClienteRepository:
    def inserir(self, cliente: Cliente):
        with con:
            con.execute(
                "INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES (?, ?, ?, ?)",
                cliente.data_for_insertion()
            )
            con.commit()