import sqlite3

DB_NAME = "escola.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

# Cria a tabela caso não exista
def init_db():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE,
                data_nascimento TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)
        conn.commit()
