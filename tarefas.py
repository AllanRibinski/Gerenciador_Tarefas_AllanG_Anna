class Tarefas:
    ESTADOS = ['Pendente', 'Desativado', 'Concluída']

    def __init__(self, task, categoria, hora=None, status='Pendente'):
        self.task = task
        self.categoria = categoria
        self.hora = hora 
        self.status = status

    def alterar_status(self, novo_status):
        if novo_status in Tarefas.ESTADOS:
            self.status = novo_status
            return f'O status da tarefa {self.task} foi alterado para {self.status}.'
        return "Status inválido."

    def __str__(self):
        hora_str = self.hora if self.hora else 'Não definida'
        return f'Nome: {self.task.ljust(30)}  Categoria: {self.categoria.ljust(30)}  Hora: {hora_str.ljust(15)}  Status: {self.status}'

