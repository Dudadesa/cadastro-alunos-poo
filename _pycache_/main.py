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
