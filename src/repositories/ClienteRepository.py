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
            cur.execute("SELECT * FROM clienteS")
            res = cur.fetchall()
            clientes: list[Cliente] = []
            for row in res:
                clientes.append(Cliente(row[1], row[2], row[3], row[4], row[0]))
            return clientes
    
    def procurar(self, id: int):
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM clientes WHERE id = ?", [id])
            res = cur.fetchone()
            return Cliente(res[1], res[2], res[3], res[4], res[0])
    
    def atualizar(self, cliente: Cliente):
        with con:
            con.execute(
                "UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, cpf = ? WHERE id = ?",
                cliente.data_for_update()
            )
            con.commit()