# TODOIST Backend

O nosso projeto é um planejador de tarefas que permite criar e organizar suas atividades.

## Getting started

Clone the repository

```bash
git clone git@github.com:antoniomesquita09/todoist-backend.git
cd todoist-backend
```

---

### Running locally

Start your python venv and install the project dependencies

```bash
python -m venv MeuEnv
source MeuEnv/bin/activate
pip3 install -r requirements.tx
```

Run migrations

```bash
python manage.py migrate
```
Create a superuser

```bash
python3 manage.py createsuperuser
```

Run the server

```bash
python manage.py runserver
```

Now the server is running on [http://localhost:8000](http://localhost:8000/docs)

You can see the **swagger** documentation on [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Running with docker

Build the docker image from a deployed docker tag from **DockerHub**

```bash
docker build -t antoniomesquita09/todoist-backend .
```

Run the deployed image locally

```bash
docker run -dp 0.0.0.0:8000:8000 antoniomesquita09/todoist-backend
```

Now the server is running on [http://localhost:8000](http://localhost:8000/docs)

You can see the **swagger** documentation on [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Funcionalidades propostas

- Criar uma tarefa (título, descrição, autor, data de criação e data de atualização)
- Editar uma tarefa (título, descrição)
- Excluir uma tarefa
- Listar tarefas
- Swagger da API

### Funcionalidades entregues

- Criar uma tarefa (título, descrição, *feita*, autor, data de criação e data de atualização)
- Editar uma tarefa (título, descrição, *feita*)
- Excluir uma tarefa
- Listar tarefas
- Swagger da API
- *Paginação da listagem de tarefas*
- *Filtro na listagem de tarefas por tarefa feita/não feita/todas*


### Limitações

- Não é possível fazer atualizações parciais das tarefas (método PATCH não implementado)
- Detalhes do autor não é retornado em nenhum dos endpoints
- Autor de uma tarefa está hardcoded, ou seja, toda tarefa é atribuída ao user de ID: 1
- Não é possível filtrar/buscar por propriedades diferentes de filter_by_done
- Fluxo de autenticação e autorização

### Tecnologias utilizadas

Desenvolvemos o backend da aplicação utilizando o framework web Django com a persistência de dados utilizando o SQLite.
