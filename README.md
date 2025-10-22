# cadastro-alunos-poo

class Aluno:
    def __init__(self, id=None, nome="", cpf="", data_nascimento="", status="ativo"):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.status = status

    def __repr__(self):
        return f"Aluno(id={self.id}, nome='{self.nome}', cpf='{self.cpf}', data_nascimento='{self.data_nascimento}', status='{self.status}')"
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
from banco import get_connection
from aluno import Aluno

# CREATE
def create_aluno(aluno: Aluno):
    sql = "INSERT INTO aluno (nome, cpf, data_nascimento, status) VALUES (?,?,?,?)"
    with get_connection() as conn:
        cur = conn.execute(sql, (aluno.nome, aluno.cpf, aluno.data_nascimento, aluno.status))
        return cur.lastrowid

# READ by ID
def read_aluno_by_id(id):
    sql = "SELECT * FROM aluno WHERE id = ?"
    with get_connection() as conn:
        cur = conn.execute(sql, (id,))
        row = cur.fetchone()
        return row

# READ all
def read_alunos():
    sql = "SELECT * FROM aluno ORDER BY id DESC"
    with get_connection() as conn:
        cur = conn.execute(sql)
        return cur.fetchall()

# UPDATE
def update_aluno(id, novos_dados):
    sql = "UPDATE aluno SET status = ? WHERE id = ?"
    with get_connection() as conn:
        cur = conn.execute(sql, (novos_dados["status"], id))
        return cur.rowcount > 0

# DELETE
def delete_aluno(id):
    sql = "DELETE FROM aluno WHERE id = ?"
    with get_connection() as conn:
        cur = conn.execute(sql, (id,))
        return cur.rowcount > 0
from aluno import Aluno
from crud import create_aluno, read_aluno_by_id, read_alunos, update_aluno, delete_aluno
from banco import init_db

def main():
    print("=== TESTANDO CRUD ===")

    # Inicializa o banco
    init_db()

    # CREATE
    aluno1 = Aluno(nome="João", cpf="12345678900", data_nascimento="2005-05-10", status="ativo")
    novo_id = create_aluno(aluno1)
    print("Novo aluno criado com ID:", novo_id)

    # READ por ID
    print("\nBuscando aluno criado...")
    print(read_aluno_by_id(novo_id))

    # READ lista
    print("\nListando todos os alunos:")
    print(read_alunos())

    # UPDATE
    print("\nAtualizando status do aluno...")
    update_aluno(novo_id, {"status": "inativo"})
    print(read_aluno_by_id(novo_id))

    # DELETE
    print("\nRemovendo aluno...")
    delete_aluno(novo_id)
    print(read_aluno_by_id(novo_id))  # Deve retornar None

if __name__ == "__main__":
    main()
