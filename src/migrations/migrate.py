from src.connections.DatabaseConnection import con
from src.migrations.ClienteMigration import ClienteMigration


def migrate():
    with con:
        con.execute(ClienteMigration().definition)
        con.commit()