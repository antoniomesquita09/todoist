# TODOIST Backend

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
