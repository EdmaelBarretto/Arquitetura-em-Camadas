# 🏗️ Arquitetura em Camadas e SOLID (DIP) — API REST de Usuários

Projeto desenvolvido para a disciplina **Análise de Projetos de Sistemas**, demonstrando a implementação de uma **API REST em Python/Flask** utilizando **Arquitetura em Camadas (Layered Architecture)** e aplicação do princípio **DIP (Dependency Inversion Principle)** do SOLID.

**Discente:** Edmael Barreto
**Turma:** ADS 44
**Profª:** Rafaella Nascimento

---

# 📋 Sobre o Projeto

Este projeto foi desenvolvido para demonstrar conceitos fundamentais de Arquitetura de Software por meio de uma API REST de gerenciamento de usuários.

Durante sua evolução foram realizadas duas atividades principais:

### ✅ Atividade 1 — Arquitetura em Camadas

Implementação de uma API estruturada nas camadas:

* Apresentação
* Serviço
* Repositório
* Domínio
* Dados

Além disso, foi adicionada a funcionalidade de cadastro de **telefone**, exigindo alterações em todas as camadas da aplicação.

### ✅ Atividade 2 — Aplicação do SOLID (DIP)

Refatoração do sistema para aplicar o princípio **Dependency Inversion Principle (DIP)**, reduzindo o acoplamento entre as camadas através da utilização de abstrações e injeção de dependências.

---

# 🎯 Objetivos de Aprendizagem

* Compreender a Arquitetura em Camadas.
* Entender a separação de responsabilidades.
* Aplicar princípios SOLID.
* Implementar Inversão de Dependência (DIP).
* Desenvolver APIs REST utilizando Flask.
* Trabalhar com persistência de dados usando SQLite.

---

# 🗂️ Estrutura do Projeto

```text
Arquitetura-em-Camadas/
│
├── app.py
│
├── apresentacao/
│   └── rotas_usuario.py
│
├── servico/
│   └── servico_usuario.py
│
├── repositorio/
│   ├── interface_repositorio.py
│   └── repositorio_usuario.py
│
├── dominio/
│   └── usuario.py
│
├── dados/
│   └── db.py
│
└── requirements.txt
```

---

# 🔄 Fluxo da Arquitetura

```text
Cliente (Postman / Browser / Curl)
              │
              ▼
Apresentação (rotas_usuario.py)
              │
              ▼
Serviço (servico_usuario.py)
              │
              ▼
Repositório (repositorio_usuario.py)
              │
              ▼
Dados (db.py)
              │
              ▼
SQLite
```

Cada camada possui responsabilidade específica e se comunica apenas com as camadas adjacentes.

---

# 🧱 Responsabilidade das Camadas

| Camada       | Responsabilidade                                   |
| ------------ | -------------------------------------------------- |
| Apresentação | Receber requisições HTTP e retornar respostas JSON |
| Serviço      | Aplicar regras de negócio                          |
| Repositório  | Realizar operações de persistência                 |
| Domínio      | Definir entidades e validações                     |
| Dados        | Gerenciar conexão com banco SQLite                 |

---

# 📱 Evolução da Funcionalidade Telefone

Durante a atividade de Arquitetura em Camadas foi adicionada a funcionalidade de telefone ao cadastro de usuários.

| Camada       | Alteração                           |
| ------------ | ----------------------------------- |
| Dados        | Inclusão da coluna telefone         |
| Domínio      | Inclusão do atributo telefone       |
| Repositório  | Atualização dos comandos SQL        |
| Serviço      | Inclusão do parâmetro telefone      |
| Apresentação | Leitura e retorno do campo telefone |

Essa atividade demonstrou como uma funcionalidade precisa atravessar todas as camadas da arquitetura.

---

# 🔄 Aplicação do SOLID — DIP

## Situação Inicial

O serviço dependia diretamente da implementação concreta do repositório.

```python
class ServicoUsuario:
    def __init__(self):
        self.repositorio = RepositorioUsuario()
```

Isso gerava forte acoplamento.

---

## Solução Aplicada

Foi criada uma abstração para o repositório.

```python
class ServicoUsuario:
    def __init__(self, repositorio: InterfaceRepositorioUsuario):
        self.repositorio = repositorio
```

Agora o serviço depende de uma abstração e não de uma implementação concreta.

---

## Arquivos Alterados para Aplicação do DIP

| Arquivo                  | Alteração                  |
| ------------------------ | -------------------------- |
| interface_repositorio.py | Criação da interface       |
| repositorio_usuario.py   | Implementação da interface |
| servico_usuario.py       | Injeção de dependência     |
| rotas_usuario.py         | Composição dos objetos     |

---

# 🧪 Endpoints Disponíveis

| Método | Endpoint           | Descrição             |
| ------ | ------------------ | --------------------- |
| POST   | /api/usuarios      | Criar usuário         |
| GET    | /api/usuarios      | Listar usuários       |
| GET    | /api/usuarios/{id} | Buscar usuário por ID |
| PUT    | /api/usuarios/{id} | Atualizar usuário     |
| DELETE | /api/usuarios/{id} | Remover usuário       |

---

# 🚀 Como Executar

## 1. Clonar o projeto

```bash
git clone https://github.com/EdmaelBarretto/Arquitetura-em-Camadas
```

```bash
cd Arquitetura-em-Camadas
```

## 2. Criar ambiente virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

## 4. Executar aplicação

```bash
python app.py
```

Servidor disponível em:

```text
http://localhost:5000
```

---

# 🛠️ Tecnologias Utilizadas

* Python 3.x
* Flask
* SQLite
* Dataclasses
* ABC (Abstract Base Classes)

---

# 🧱 Princípios SOLID Aplicados

| Princípio | Aplicação                                       |
| --------- | ----------------------------------------------- |
| SRP       | Separação das responsabilidades por camada      |
| OCP       | Estrutura preparada para extensão               |
| LSP       | Implementações respeitam contratos              |
| ISP       | Interfaces específicas                          |
| DIP       | Dependência de abstrações ao invés de concretos |

---

# 📚 Conceitos Demonstrados

* Arquitetura em Camadas
* API REST
* Flask
* SQLite
* CRUD
* SOLID
* Dependency Injection
* Dependency Inversion Principle (DIP)

---

# 👨‍💻 Autor

**Edmael Barreto**

Curso de Análise e Desenvolvimento de Sistemas — ADS 44

Disciplina: Análise de Projetos de Sistemas

Profª Rafaella Nascimento
