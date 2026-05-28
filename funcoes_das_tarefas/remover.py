def remover_tarefa(tarefas):
    nome = input("Digite o nome da tarefa a ser removida: ")

    for indice, tarefa in enumerate(tarefas):
        if tarefa["nome"] == nome:
            tarefas.pop(indice)
            print("Tarefa removida com sucesso!")
            return

    print("Tarefa não encontrada.")
