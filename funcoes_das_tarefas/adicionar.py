def adicionar_tarefa(tarefas):
    nome = input("Digite o nome da tarefa: ").strip("")
    descricao = input("Digite a descrição da tarefa: ").strip("")

    if not nome:
        print("O nome da tarefa não pode ser vazio.")
        return
    if not descricao:
        print("A descrição da tarefa não pode ser vazia.")
        return
    
    tarefas.append({"nome": nome, "descricao": descricao})
    print("Tarefa adicionada com sucesso!")

    