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
