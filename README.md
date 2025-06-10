# newsIA

This repository contains the initial layout for a project with a separate
backend and frontend. Development and future deployment will rely on Docker.

## Getting Started

1. Clone the repository.
2. Copy `.env.example` to `.env` and adjust values if necessary.
3. Run the project using Docker Compose:

   ```bash
   docker compose up --build
   ```

This command will build and start the backend and frontend containers
according to `docker-compose.yml`.

## Installing Dependencies

Dependencies will be installed automatically when the Docker images are
built. You will need Docker and Docker Compose installed on your machine.

## Project Structure

```
backend/   # Backend code and Dockerfile
frontend/  # Frontend code and Dockerfile
docker-compose.yml
.env.example
README.md
```

Both `backend` and `frontend` directories are currently empty and will be
populated in future commits.

