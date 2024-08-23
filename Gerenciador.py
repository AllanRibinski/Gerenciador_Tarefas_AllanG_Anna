import os
from tarefas import Tarefas

class GerenciadorTarefas:
    def __init__(self):
        self.usuario = input("Digite o seu nome: ")
        self.tarefas = [
            Tarefas('Comprar Leite', 'Supermercado', '10:00', 'Pendente'),
        ]

    def finalizar_app(self):
        os.system("clear")
        os.system("cls")
        print("Finalizando o app\n")

    def voltar_menu_principal(self):
        input("Digite uma tecla para voltar ao menu principal: ")

    def mostrar_subtitulo(self, texto):
        os.system("clear")
        os.system("cls")
        linha = '*' * len(texto)
        print(linha)
        print(texto)
        print(linha)
        print()

    def testar_tarefa(self):
        self.listarTarefas()
        self.voltar_menu_principal()    

    def escolher_opcoes(self):
        self.mostrar_subtitulo(f"Gerenciador De Tarefas - {self.usuario}")
        print("1 - Adicionar/Remover Tarefa")
        print("2 - Alterar Status")
        print("3 - Editar Tarefas")
        print("4 - Listar Tarefas")
        print("5 - Listar por Categoria")
        print("6 - Sair\n")

    def opcao_invalida(self):
        self.mostrar_subtitulo("Opção inválida\n".ljust(20))
        self.voltar_menu_principal()

    def cadastrar_nova_tarefa(self):
        nome_da_tarefa = input("Digite o nome da nova tarefa: ")
        categoria = input(f'Digite a categoria da tarefa {nome_da_tarefa}: ')
        hora = input(f'Digite a hora da tarefa (formato HH:MM, opcional): ')
        tarefa_nova = Tarefas(nome_da_tarefa, categoria, hora)
        self.tarefas.append(tarefa_nova)
        print(f"Você cadastrou a tarefa: {nome_da_tarefa}")

    def remover_tarefa(self):
        self.listarTarefas()
        nome_tarefa = input("Digite o nome da tarefa que deseja remover: ")
        tarefa_encontrada = False

        for tarefa in self.tarefas:
            if nome_tarefa.lower() == tarefa.task.lower():
                self.tarefas.remove(tarefa)
                tarefa_encontrada = True
                print(f"A tarefa '{nome_tarefa}' foi removida com sucesso.")
                break

        if not tarefa_encontrada:
            print("A tarefa não foi encontrada.")

    def alterar_status(self):
        self.mostrar_subtitulo("Alterando o estado da tarefa".ljust(20))
        self.listarTarefas()
        nome_tarefa = input("Digite o nome da tarefa que deseja alterar: ")
        tarefa_encontrada = False

        for tarefa in self.tarefas:
            if nome_tarefa.lower() == tarefa.task.lower():
                tarefa_encontrada = True
                print("Escolha o novo status:")
                for i, estado in enumerate(Tarefas.ESTADOS, start=1):
                    print(f"{i} - {estado}")

                try:
                    opcao = int(input("Digite o número do status desejado: "))
                    if 1 <= opcao <= len(Tarefas.ESTADOS):
                        tarefa.status = Tarefas.ESTADOS[opcao - 1]
                        print(f"O status da tarefa '{tarefa.task}' foi alterado para '{tarefa.status}'.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Por favor, digite um número válido.")
                break

        if not tarefa_encontrada:
            print("A tarefa não foi encontrada.")

        self.voltar_menu_principal()

    def listarTarefas(self):
        self.mostrar_subtitulo('Listando as Tarefas'.ljust(20))
        print("Nome:".ljust(37), "Categoria:".ljust(42), "Hora:".ljust(22), "Status:".ljust(20))
        
        if self.tarefas:
            for tarefa in self.tarefas:
                print(tarefa)
        else:
            print("Nenhuma tarefa encontrada.")    

    def editar_tarefas(self):
        self.listarTarefas()
        nome_tarefa = input("Digite o nome da tarefa que deseja editar: ")
        tarefa_encontrada = False

        for tarefa in self.tarefas:
            if nome_tarefa.lower() == tarefa.task.lower():
                tarefa_encontrada = True
                print("O que deseja alterar?")
                print("1 - Nome")
                print("2 - Categoria")
                print("3 - Hora")
                opcao = int(input("Digite a opção desejada: "))

                if opcao == 1:
                    novo_nome = input("Digite o novo nome da tarefa: ")
                    tarefa.task = novo_nome
                elif opcao == 2:
                    nova_categoria = input("Digite a nova categoria da tarefa: ")
                    tarefa.categoria = nova_categoria
                elif opcao == 3:
                    nova_hora = input("Digite a nova hora da tarefa (formato HH:MM): ")
                    tarefa.hora = nova_hora
                elif opcao == 4:
                    print("Escolha o novo status:")
                    for i, estado in enumerate(Tarefas.ESTADOS, start=1):
                        print(f"{i} - {estado}")

                    try:
                        opcao_status = int(input("Digite o número do status desejado: "))
                        if 1 <= opcao_status <= len(Tarefas.ESTADOS):
                            tarefa.status = Tarefas.ESTADOS[opcao_status - 1]
                            print(f"O status da tarefa '{tarefa.task}' foi alterado para '{tarefa.status}'.")
                        else:
                            print("Opção inválida.")
                    except ValueError:
                        print("Por favor, digite um número válido.")
                else:
                    print("Opção inválida.")

                print(f"Tarefa '{tarefa.task}' atualizada com sucesso.")
                break

        if not tarefa_encontrada:
            print("A tarefa não foi encontrada.")

    def listar_Categoria(self):
        self.mostrar_subtitulo('Listar Tarefas por Categoria'.ljust(20))
    
    
        categorias = set(tarefa.categoria for tarefa in self.tarefas)
    
        if categorias:
            print("Categorias disponíveis:")
            categoria_lista = list(categorias)  
            for i, categoria in enumerate(categoria_lista, start=1):
                print(f"{i} - {categoria}")
        
            try:
                opcao_categoria = int(input("Digite o número da categoria desejada: "))
            
                if 1 <= opcao_categoria <= len(categoria_lista):
                    categoria_escolhida = categoria_lista[opcao_categoria - 1]
                    tarefas_encontradas = False

                    self.mostrar_subtitulo(f'Tarefas na Categoria: {categoria_escolhida}'.ljust(20))
                    print("Nome:".ljust(37), "Categoria:".ljust(42), "Hora:".ljust(22), "Status:".ljust(20))
                
                    for tarefa in self.tarefas:
                        if tarefa.categoria.lower() == categoria_escolhida.lower():
                            print(tarefa)
                            tarefas_encontradas = True

                    if not tarefas_encontradas:
                        print(f"Nenhuma tarefa encontrada na categoria '{categoria_escolhida}'.")
                else:
                    print("Número de categoria inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")
        
        else:
            print("Nenhuma categoria encontrada.")

        self.voltar_menu_principal()


    def main(self):
        while True:
            try:
                self.escolher_opcoes()
                opcao_digitada = int(input("Digite a opção desejada: "))
                
                if opcao_digitada == 1:
                    self.mostrar_subtitulo("Escolha uma ação".ljust(20))
                    print("1 - Adicionar Tarefa")
                    print("2 - Remover Tarefa")
                    acao = int(input("Digite a opção desejada: "))
                    
                    if acao == 1:
                        print("Você escolheu adicionar tarefa\n")
                        self.cadastrar_nova_tarefa()
                    elif acao == 2:
                        print("Você escolheu remover tarefa\n")
                        self.remover_tarefa()
                    else:
                        print("Opção inválida.")
                
                elif opcao_digitada == 2:
                    self.alterar_status()
                elif opcao_digitada == 3:
                    self.editar_tarefas()
                elif opcao_digitada == 4:
                    self.testar_tarefa()
                elif opcao_digitada == 5:
                    self.listar_Categoria()
                elif opcao_digitada == 6:
                    print("Você escolheu sair do aplicativo\n")
                    self.finalizar_app()
                    break
                else:
                    self.opcao_invalida()
                
            except ValueError:
                print("Por favor, digite um número válido.")

if __name__ == "__main__":
    programa = GerenciadorTarefas()
    programa.main()
