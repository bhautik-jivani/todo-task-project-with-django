# Todo Task - Backend

This is the backend of the Todo Task application built using Django, running inside Docker with PostgreSQL as the database, Nginx as the web server, and PgAdmin for database administration.

## Project Setup

### 1. Create Environment Configuration

Create an `.env.local` file in the root directory of the project and add the following environment variables:

```bash
POSTGRES_DB=<db_name>
POSTGRES_USER=<db_username>
POSTGRES_PASSWORD=<db_password>
POSTGRES_HOST=postgres_db # docker service name
POSTGRES_PORT=5432

PGADMIN_DEFAULT_EMAIL=<custom_email>  # Replace with your preferred email
PGADMIN_DEFAULT_PASSWORD=<custom_password>
```

### 2. Start Docker Services

Use the following command to start the required services using Docker Compose:

```bash
docker compose up -d
```

### 3. Run Database Migrations

After the Docker services are up, run the following commands to create and apply initial migrations for the Django backend:

```bash
docker exec -it todo_task_backend bash -c "python manage.py makemigrations"

docker exec -it todo_task_backend bash -c "python manage.py migrate"
```

### 4. Collect Static Files

Collect static files (for Django Admin and Django Rest Framework) using the following command:

```bash
docker exec -it todo_task_backend bash -c "python manage.py collectstatic --no-input"
```

## Running the Project

To access the Swagger documentation and explore the available APIs, open your browser and go to:

```bash
http://localhost:80/swagger/
```

This will provide an interactive interface to test and explore all the API endpoints of the Todo Task application.