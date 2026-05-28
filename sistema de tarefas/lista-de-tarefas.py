import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from funcoes_das_tarefas.adicionar import adicionar_tarefa
from funcoes_das_tarefas.listar import listar_tarefas
from funcoes_das_tarefas.remover import remover_tarefa
from funcoes_das_tarefas.sair import sair_da_aplicacao

caminho_arquivo = r"C:\Users\kaike\Desktop\lista de tarefas\sistema de tarefas\tarefas.json"


def carregar_tarefas():
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return "Não encontrado. Criando um novo arquivo."
    except json.JSONDecodeError:
        return "Arquivo corrompido. Criando um novo arquivo."


def salvar_tarefas(tarefas):
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)


tarefas = carregar_tarefas()

while True:
    print("\nseja bem-vindo ao sistema de tarefas!")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_tarefa(tarefas)
        salvar_tarefas(tarefas)

    elif escolha == "2":
        listar_tarefas(tarefas)

    elif escolha == "3":
        remover_tarefa(tarefas)
        salvar_tarefas(tarefas)

    elif escolha == "4":
        salvar_tarefas(tarefas)
        sair_da_aplicacao()
        break

    else:
        print("Opção inválida. Tente novamente.")

