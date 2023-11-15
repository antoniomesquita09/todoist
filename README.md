# TODOIST Backend

## Getting started

Clone the repository

```bash
git clone git@github.com:antoniomesquita09/todoist-backend.git
cd todoist-backend
```

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

Run the server

```bash
python manage.py runserver
```

Now the server is running on [http://localhost:8000](http://localhost:8000/docs)

You can see the **swagger** documentation on [http://localhost:8000/docs](http://localhost:8000/docs)