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
    
    def listar(self):
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM clientes ORDER BY nome")
            res = cur.fetchall()
            clientes: list[Cliente] = []
            for row in res:
                clientes.append(Cliente(row[1], row[2], row[3], row[4], row[0]))
            return clientes