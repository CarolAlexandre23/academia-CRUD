from app.database.connection import get_db
from app.models.matricula_model import MatriculaModel

class MatriculaRepository:
    
    def get_all_matriculas(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.id, m.data_inicio, m.plano, m.aluno_id, a.nome
            FROM matricula m
            JOIN aluno a ON m.aluno_id = a.id
        """)
        rows = cursor.fetchall()
        matriculas = []
        for row in rows:
            matricula = MatriculaModel(
                id=row[0],
                data_inicio=row[1],
                plano=row[2],
                aluno_id=row[3]
            )
            matricula.aluno_nome = row[4]
            matriculas.append(matricula)
        return matriculas
    
    def get_matricula_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.id, m.data_inicio, m.plano, m.aluno_id, a.nome
            FROM matricula m
            JOIN aluno a ON m.aluno_id = a.id
            WHERE m.id = ?
        """, (id,))
        row = cursor.fetchone()
        if row:
            matricula = MatriculaModel(
                id=row[0],
                data_inicio=row[1],
                plano=row[2],
                aluno_id=row[3]
            )
            matricula.aluno_nome = row[4]
            return matricula
        return None
        
    def create_matricula(self, matricula):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO matricula (data_inicio, plano, aluno_id)
            VALUES (?, ?, ?)
        """, (matricula.get_data_inicio(), matricula.get_plano(), matricula.get_aluno_id()))
        connection.commit()
        
    def update_matricula(self, matricula):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE matricula
            SET data_inicio = ?, plano = ?, aluno_id = ?
            WHERE id = ?
        """, (matricula.get_data_inicio(), matricula.get_plano(), matricula.aluno_id(), matricula.get_id()))
        connection.commit()
        
    def delete_matricula(self, matricula_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM matricula WHERE id = ?", (matricula_id,))
        connection.commit()

    def get_matriculas_by_aluno_id(self, aluno_id):
        if aluno_id is None:
            raise ValueError("O ID do aluno é obrigatório.")

        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM matricula WHERE aluno_id = ?", (aluno_id,))
        rows = cursor.fetchall()

        return [
            MatriculaModel(
                id=row[0],
                data_inicio=row[1],
                plano=row[2],
                aluno_id=row[3]
            )
            for row in rows
        ]
