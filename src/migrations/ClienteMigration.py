class ClienteMigration:
    def __init__(self):
        self.definition = """
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER NOT NULL PRIMARY KEY,
    nome VARCHAR (32) NOT NULL,
    sobrenome VARCHAR (64) NOT NULL,
    email VARCHAR (64) NOT NULL UNIQUE,
    cpf VARCHAR (14) NOT NULL UNIQUE
);
        """