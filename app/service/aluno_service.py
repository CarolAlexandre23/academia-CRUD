from app.repository.aluno_repository import AlunoRepository
from app.models.aluno_model import AlunoModel
from app.repository.matricula_repository import MatriculaRepository
from datetime import datetime, date



class AlunoService:
    def __init__(self):
        self.aluno_repository = AlunoRepository()
        self.matricula_repository = MatriculaRepository()

    def get_all_alunos(self):
        return self.aluno_repository.get_all_alunos()

    def get_aluno_by_id(self, id):
        return self.aluno_repository.get_aluno_by_id(id)
    
    def validate_date(self, date_str):
        try:
            data_nascimento = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Data inválida. Use o formato YYYY-MM-DD.")
        
        hoje = date.today()
        if data_nascimento > hoje:
            raise ValueError("A data de nascimento não pode ser no futuro.")

        idade = hoje.year - data_nascimento.year - (
            (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
        )
        if idade > 130:
            raise ValueError("Idade inválida. Por favor, verifique a data de nascimento.")

        return data_nascimento

    def create_aluno(self, aluno: AlunoModel):
        if not aluno.get_nome():
            raise ValueError("O nome é obrigatório para criar um aluno.")
        if not aluno.get_telefone():
            raise ValueError("O telefone é obrigatório para criar um aluno.")
        if aluno.get_data_nascimento():
            # valida a data de nascimento e seta no aluno
            aluno.set_data_nascimento(self.validate_date(aluno.get_data_nascimento()))
        self.aluno_repository.create_aluno(aluno)

    def update_aluno(self, aluno: AlunoModel):
        if aluno.get_id() is None:
            raise ValueError("O ID do aluno é obrigatório para atualizar.")
        if not aluno.get_nome():
            raise ValueError("O nome é obrigatório para atualizar o aluno.")
        if not aluno.get_telefone():
            raise ValueError("O telefone é obrigatório para atualizar o aluno.")
        if aluno.get_data_nascimento():
            aluno.set_data_nascimento(self.validate_date(aluno.get_data_nascimento()))
        self.aluno_repository.update_aluno(aluno)


    def delete_aluno(self, id):
        if id is None:
            raise ValueError("O ID do aluno é obrigatório para deletar.")

        # Verifica se o aluno possui matrículas
        matriculas = self.matricula_repository.get_matriculas_by_aluno_id(id)
        if matriculas:
            raise ValueError("Não é possível deletar o aluno porque ele possui matrícula(s) vinculada(s).")

        self.aluno_repository.delete_aluno(id)
