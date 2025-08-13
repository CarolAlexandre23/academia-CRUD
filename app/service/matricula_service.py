from app.repository.matricula_repository import MatriculaRepository
from app.models.matricula_model import MatriculaModel

class MatriculaService:
    def __init__(self):
        self.matricula_repository = MatriculaRepository()

    def get_all_matriculas(self):
        return self.matricula_repository.get_all_matriculas()

    def get_matricula_by_id(self, id):
        return self.matricula_repository.get_matricula_by_id(id)

    def create_matricula(self, matricula: MatriculaModel):
        if matricula.get_aluno_id() is None:
            raise ValueError("O ID do aluno é obrigatório para criar uma matrícula.")
        if not matricula.get_data_inicio():
            raise ValueError("A data de início é obrigatória para criar uma matrícula.")
        if not matricula.get_plano():
            raise ValueError("O plano é obrigatório para criar uma matrícula.")
        self.matricula_repository.create_matricula(matricula)

    def update_matricula(self, matricula: MatriculaModel):
        if matricula.get_id() is None:
            raise ValueError("O ID da matrícula é obrigatório para atualizar.")
        if matricula.get_aluno_id() is None:
            raise ValueError("O ID do aluno é obrigatório para atualizar a matrícula.")
        if not matricula.get_data_inicio():
            raise ValueError("A data de início é obrigatória para atualizar a matrícula.")
        if not matricula.get_plano():
            raise ValueError("O plano é obrigatório para atualizar a matrícula.")
        self.matricula_repository.update_matricula(matricula)

    def delete_matricula(self, id):
        if id is None:
            raise ValueError("O ID da matrícula é obrigatório para deletar.")
        self.matricula_repository.delete_matricula(id)
        
