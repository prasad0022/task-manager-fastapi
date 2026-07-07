# Task Manager API

A RESTful Task Manager API built with **FastAPI** to learn modern backend development. This project demonstrates CRUD operations, PostgreSQL integration, SQLAlchemy ORM, Alembic migrations, and Docker-based deployment.

## Features

- Create, Read, Update (PATCH), and Delete tasks
- FastAPI with automatic Swagger documentation
- PostgreSQL database integration
- SQLAlchemy ORM
- Alembic database migrations
- Environment variable configuration using `.env`
- Dockerized application
- RESTful API design

## Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn
- Docker

## Project Structure

```text
.
├── alembic/
├── app/
│   ├── routers/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── .env
├── .dockerignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd task-manager
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql://postgres:<password>@localhost:5432/task_manager
```

### Run Database Migrations

```bash
alembic upgrade head
```

### Start the Development Server

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

| Method | Endpoint           | Description             |
| ------ | ------------------ | ----------------------- |
| GET    | `/tasks`           | Get all tasks           |
| GET    | `/tasks/{task_id}` | Get a task by ID        |
| POST   | `/tasks`           | Create a new task       |
| PATCH  | `/tasks/{task_id}` | Partially update a task |
| DELETE | `/tasks/{task_id}` | Delete a task           |
| GET    | `/health`          | Health check            |

## Learning Objectives

This project was built to gain hands-on experience with:

- FastAPI fundamentals
- REST API development
- Database design with PostgreSQL
- SQLAlchemy ORM
- Alembic migrations
- Docker containerization
- Production-ready backend architecture

## License

This project is created for learning and educational purposes.
