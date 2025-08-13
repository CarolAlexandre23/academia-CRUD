from app import app
from flask import render_template, request, redirect, url_for

from app.models.aluno_model import AlunoModel
from app.service.aluno_service import AlunoService
from app.models.matricula_model import MatriculaModel
from app.service.matricula_service import MatriculaService

aluno_service = AlunoService()
matricula_service = MatriculaService()


# Página inicial
@app.route('/')
def index():
    return redirect(url_for('listar_alunos'))


# ============================
# ROTAS PARA ALUNO
# ============================

@app.route('/alunos')
def listar_alunos():
    alunos = aluno_service.get_all_alunos()
    return render_template('alunos/list_aluno.html', alunos=alunos)


@app.route('/alunos/novo', methods=['GET', 'POST'])
def criar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        data_nascimento = request.form['data_nascimento']

        aluno_service.create_aluno(AlunoModel(
            id=None,
            nome=nome,
            telefone=telefone,
            data_nascimento=data_nascimento
        ))
        return redirect(url_for('listar_alunos'))
    return render_template('alunos/form_aluno.html')


@app.route('/alunos/editar/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = aluno_service.get_aluno_by_id(id)
    if request.method == 'POST':
        aluno_service.update_aluno(AlunoModel(
            id=id,
            nome=request.form['nome'],
            telefone=request.form['telefone'],
            data_nascimento=request.form['data_nascimento']
        ))
        return redirect(url_for('listar_alunos'))
    return render_template('alunos/form_aluno.html', aluno=aluno)


@app.route('/alunos/excluir/<int:id>')
def excluir_aluno(id):
    aluno_service.delete_aluno(id)
    return redirect(url_for('listar_alunos'))


# ============================
# ROTAS PARA MATRÍCULA
# ============================

@app.route('/matriculas')
def listar_matriculas():
    matriculas = matricula_service.get_all_matriculas()
    return render_template('matriculas/list_matricula.html', matriculas=matriculas)


@app.route('/matriculas/nova', methods=['GET', 'POST'])
def criar_matricula():
    alunos = aluno_service.get_all_alunos()
    if request.method == 'POST':
        aluno_id = request.form['aluno_id']
        data_inicio = request.form['data_inicio']
        plano = request.form['plano']

        matricula_service.create_matricula(MatriculaModel(
            id=None,
            aluno_id=aluno_id,
            data_inicio=data_inicio,
            plano=plano
        ))
        return redirect(url_for('listar_matriculas'))
    return render_template('matriculas/form_matricula.html', alunos=alunos)


@app.route('/matriculas/editar/<int:id>', methods=['GET', 'POST'])
def editar_matricula(id):
    matricula = matricula_service.get_matricula_by_id(id)
    alunos = aluno_service.get_all_alunos()
    if request.method == 'POST':
        matricula_service.update_matricula(MatriculaModel(
            id=id,
            aluno_id=request.form['aluno_id'],
            data_inicio=request.form['data_inicio'],
            plano=request.form['plano']
        ))
        return redirect(url_for('listar_matriculas'))
    return render_template('matriculas/form_matricula.html', matricula=matricula, alunos=alunos)


@app.route('/matriculas/excluir/<int:id>')
def excluir_matricula(id):
    matricula_service.delete_matricula(id)
    return redirect(url_for('listar_matriculas'))
