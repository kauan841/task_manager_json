# 🗂️ Task Manager (Sistema de Tarefas em Python)

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Um sistema de gerenciamento de tarefas desenvolvido em Python, com armazenamento em JSON e arquitetura modular.

---

## 📌 Sobre o projeto

Este projeto foi criado com o objetivo de praticar organização de código, lógica de programação, manipulação de arquivos JSON e estruturação de projetos em Python.

---

## ⚙️ Funcionalidades

✔️ Adicionar tarefas  
📋 Listar tarefas  
❌ Remover tarefas  
💾 Salvar automaticamente em JSON  
🔄 Carregar tarefas ao iniciar o programa  
🚪 Sair da aplicação  

---

## 📂 Estrutura do projeto

lista_de_tarefas/  
│  
├── sistema_de_tarefas/  
│   ├── main.py  
│   ├── tarefas.json  
│  
├── funcoes_das_tarefas/  
│   ├── adicionar.py  
│   ├── listar.py  
│   ├── remover.py  
│   ├── sair.py  

---


---

## 🧠 Código principal (main.py) — Como aparece para o usuário

Quando o programa é executado, o usuário interage diretamente pelo terminal.

Exemplo da interface:

Seja bem-vindo ao sistema de tarefas!
1 - Adicionar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Sair

Escolha uma opção: 1

Após escolher uma opção, o sistema executa a ação correspondente:

- Se escolher **1**, o sistema pede a descrição da tarefa
- Se escolher **2**, lista todas as tarefas salvas
- Se escolher **3**, remove uma tarefa 
- Se escolher **4**, salva os dados e encerra o programa

Esse fluxo se repete até o usuário escolher sair.


---

## 💾 Exemplo de armazenamento (tarefas.json)

[
  {
    "id": 1,
    "tarefa": "Estudar Python"
  },
  {
    "id": 2,
    "tarefa": "Fazer exercícios"
  }
]

---

## 🧠 Melhorias futuras

- Interface gráfica (Tkinter ou Web)
- Banco de dados SQLite
- Sistema de categorias
- Sistema de prioridade (alta, média, baixa)
- Refatorar imports (remover sys.path.append)
- Transformar em API com Flask

---

## ⚠️ Observações importantes

- Usa `sys.path.append` para importações entre pastas
- Caminho do JSON está como absoluto (pode ser melhorado com Path)
- Projeto focado em aprendizado e evolução em Python

---

## 👨‍💻 Autor

Kauan 🚀  
Projeto desenvolvido para prática de Python 
