# Portfolio Website - Nora Nassir

This Django-based web application is skeleton to showcase my work, projects, and contact information in the future. The site is built responsive design using Django, PostgreSQL, Docker, and several other tools for development and deployment.

## Features

- **Dynamic Project Management:** Users can view various projects, complete with descriptions, images, and source links.
- **Custom User Authentication:** A custom user model allows for personalized authentication.
- **REST API with Documentation:** API is built with Django Rest Framework (DRF) and documented using **DRF Spectacular**.
- **Responsive Frontend:** The site uses Bootstrap for mobile responsiveness and a clean design.
- **Dockerized Application:** The entire project is containerized using Docker for easy deployment.

### Requirements

- Docker and Docker Compose
- PostgreSQL
- Python 3.9

## Technologies

- **Django 3.2.25:** Backend framework for web development.
- **Django Rest Framework (DRF):** For building APIs.
- **PostgreSQL 13-alpine:** The database for data storage.
- **DRF Spectacular:** Automatic API documentation.
- **Docker:** For containerizing the app.
- **Bootstrap 5.3:** Frontend CSS framework.
- **WhiteNoise:** To handle static files in production.

## API Endpoints

The API exposes the following endpoints:

- `GET /api/projects/` - Get a list of all projects.
- `GET /api/projects/{id}/` - Get details of a specific project.
- `POST /api/projects/` - Add a new project (authenticated users).
- `PUT /api/projects/{id}/` - Update a project (authenticated users).
- `DELETE /api/projects/{id}/` - Delete a project (authenticated users).

API Documentation can be accessed at `/api/docs/`.
