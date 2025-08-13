# Academia Nicolaus Fitness

Este é um sistema simples desenvolvido em **Flask + SQLite** para gerenciar **alunos** e **matrículas**.  
O projeto segue a arquitetura de **Models, Repositories e Services**, com CRUD completo para ambas as entidades.

---

## 📌 Funcionalidades

- **CRUD de Alunos**
  - Criar, editar, listar e excluir alunos.
  - Validação para não excluir alunos com matrículas ativas.

- **CRUD de Matrículas**
  - Criar, editar, listar e excluir matrículas.
  - Seleção de aluno ao criar a matrícula.


1. Crie o ambiente virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
2. Instale as dependências:
    ```bash
    pip install --upgrade pip
    pip install Flask
    ```
3. Execute o projeto:
    ```bash
    python run.py
    ```