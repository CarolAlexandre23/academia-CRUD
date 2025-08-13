CREATE TABLE aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    data_nascimento DATE NOT NULL
);

CREATE TABLE matricula (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_inicio DATE NOT NULL,
    plano TEXT NOT NULL, 
    aluno_id INTEGER NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES aluno (id)
);
