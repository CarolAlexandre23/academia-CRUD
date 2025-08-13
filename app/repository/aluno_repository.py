from app.database.connection import get_db
from app.models.aluno_model import AlunoModel

class AlunoRepository:

    def get_all_alunos(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, nome, data_nascimento, telefone
            FROM aluno
        """)
        rows = cursor.fetchall()
        alunos = []
        for row in rows:
            aluno = AlunoModel(
                id=row[0],
                nome=row[1],
                data_nascimento=row[2],
                telefone=row[3]
            )
            alunos.append(aluno)
        return alunos

    def get_aluno_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, nome, data_nascimento, telefone
            FROM aluno
            WHERE id = ?
        """, (id,))
        row = cursor.fetchone()
        if row:
            return AlunoModel(
                id=row[0],
                nome=row[1],
                data_nascimento=row[2],
                telefone=row[3]
            )
        return None

    def create_aluno(self, aluno):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO aluno (nome, data_nascimento, telefone)
            VALUES (?, ?, ?)
        """, (aluno.get_nome(), aluno.get_data_nascimento(), aluno.get_telefone()))
        connection.commit()

    def update_aluno(self, aluno):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE aluno
            SET nome = ?, data_nascimento = ?, telefone = ?
            WHERE id = ?
        """, (aluno.get_nome(), aluno.get_data_nascimento(), aluno.get_telefone(), aluno.get_id()))
        connection.commit()

    def delete_aluno(self, aluno_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM aluno WHERE id = ?", (aluno_id,))
        connection.commit()

    def get_matriculas_by_aluno_id(self, aluno_id):
        """Retorna todas as matrículas associadas a um aluno específico"""
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM matricula WHERE aluno_id = ?", (aluno_id,))
        return cursor.fetchall()
