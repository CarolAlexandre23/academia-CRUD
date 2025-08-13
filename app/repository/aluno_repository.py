from app.database.connection import get_db
from app.models.aluno_model import AlunoModel

class AlunoRepository:

    def get_all_alunos(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, nome, idade, telefone
            FROM aluno
        """)
        rows = cursor.fetchall()
        alunos = []
        for row in rows:
            aluno = AlunoModel(
                id=row[0],
                nome=row[1],
                idade=row[2],
                telefone=row[3]
            )
            alunos.append(aluno)
        return alunos

    def get_aluno_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, nome, idade, telefone
            FROM aluno
            WHERE id = ?
        """, (id,))
        row = cursor.fetchone()
        if row:
            return AlunoModel(
                id=row[0],
                nome=row[1],
                idade=row[2],
                telefone=row[3]
            )
        return None

    def create_aluno(self, aluno):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO aluno (nome, idade, telefone)
            VALUES (?, ?, ?)
        """, (aluno.get_nome(), aluno.get_idade(), aluno.get_telefone()))
        connection.commit()

    def update_aluno(self, aluno):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE aluno
            SET nome = ?, idade = ?, telefone = ?
            WHERE id = ?
        """, (aluno.get_nome(), aluno.get_idade(), aluno.get_telefone(), aluno.get_id()))
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
        cursor.execute("""
            SELECT id, id_aluno, id_curso, data_matricula
            FROM matricula
            WHERE id_aluno = ?
        """, (aluno_id,))
        rows = cursor.fetchall()
        return rows 
