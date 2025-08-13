from app.database.connection import get_db
from app.models.matricula_model import MatriculaModel

class MatriculaRepository:
    
    def get_all_matriculas(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.id, m.data_inicio, m.plano, m.id_aluno, a.nome
            FROM matricula m
            JOIN aluno a ON m.id_aluno = a.id
        """)
        rows = cursor.fetchall()
        matriculas = []
        for row in rows:
            matricula = MatriculaModel(
                id=row[0],
                data_inicio=row[1],
                plano=row[2],
                id_aluno=row[3]
            )
            matricula.aluno_nome = row[4]
            matriculas.append(matricula)
        return matriculas
    
    def get_matricula_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.id, m.data_inicio, m.plano, m.id_aluno, a.nome
            FROM matricula m
            JOIN aluno a ON m.id_aluno = a.id
            WHERE m.id = ?
        """, (id,))
        row = cursor.fetchone()
        if row:
            matricula = MatriculaModel(
                id=row[0],
                data_inicio=row[1],
                plano=row[2],
                id_aluno=row[3]
            )
            matricula.aluno_nome = row[4]
            return matricula
        return None
        
    def create_matricula(self, matricula):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO matricula (data_inicio, plano, id_aluno)
            VALUES (?, ?, ?)
        """, (matricula.get_data_inicio(), matricula.get_plano(), matricula.get_id_aluno()))
        connection.commit()
        
    def update_matricula(self, matricula):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE matricula
            SET data_inicio = ?, plano = ?, id_aluno = ?
            WHERE id = ?
        """, (matricula.get_data_inicio(), matricula.get_plano(), matricula.get_id_aluno(), matricula.get_id()))
        connection.commit()
        
    def delete_matricula(self, matricula_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM matricula WHERE id = ?", (matricula_id,))
        connection.commit()
