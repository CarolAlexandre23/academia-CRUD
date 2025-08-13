class MatriculaModel:
    def __init__(self, id, data_inicio, plano, aluno_id):
        self.__id = id
        self.__data_inicio = data_inicio
        self.__plano = plano
        self.__aluno_id = aluno_id

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_data_inicio(self):
        return self.__data_inicio
    
    def set_data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio

    def get_plano(self):
        return self.__plano
    
    def set_plano(self, plano):
        self.__plano = plano

    def get_aluno_id(self):
        return self.__aluno_id
    
    def set_aluno_id(self, aluno_id):
        self.__aluno_id = aluno_id
