def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("Lista de tarefas:")
    for tarefa in tarefas:
        print(f"- {tarefa['nome']}: {tarefa['descricao']}")
