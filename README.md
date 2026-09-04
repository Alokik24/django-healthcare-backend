# Django Healthcare Backend

## Overview

Healthcare backend built with Django, Django REST Framework, PostgreSQL, and JWT authentication.

The application provides APIs for:

* User registration and login
* Patient management
* Doctor management
* Patient–doctor mappings
* JWT-based authentication
* Validation and error handling

## Technologies

* Python
* Django
* Django REST Framework
* PostgreSQL
* djangorestframework-simplejwt
* python-dotenv

## Project Structure

```text
django-healthcare-backend/
│
├── apps/
│   ├── accounts/
│   ├── patients/
│   ├── doctors/
│   └── mappings/
│
├── config/
├── postman/
│   └── Healthcare Backend.postman_collection.json
│
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Requirements

Before running the project, make sure you have:

* Python 3.x
* PostgreSQL
* pip
* Git

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd django-healthcare-backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
venv\Scripts\activate
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root.

Use `.env.example` as a template.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=your-postgresql-password
DB_HOST=localhost
DB_PORT=5432
```

**Do not commit `.env` to GitHub.**

### 6. Configure PostgreSQL

Create a PostgreSQL database and user.

Example:

```text
Database: healthcare_db
User: healthcare_user
Port: 5432
```

Place the PostgreSQL credentials in the `.env` file.

Make sure the PostgreSQL server is running before starting Django.

### 7. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Authentication

The API uses JWT authentication.

### Register

```http
POST /api/auth/register/
```

Example request:

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "StrongPassword123!"
}
```

### Login

```http
POST /api/auth/login/
```

Example request:

```json
{
    "email": "john@example.com",
    "password": "StrongPassword123!"
}
```

The login response provides an access token and refresh token.

### Authentication Header

Protected endpoints require the access token:

```text
Authorization: Bearer <access_token>
```

## Patient APIs

All patient endpoints require authentication.

| Method | Endpoint              | Description                                     |
| ------ | --------------------- | ----------------------------------------------- |
| POST   | `/api/patients/`      | Create a patient                                |
| GET    | `/api/patients/`      | List patients created by the authenticated user |
| GET    | `/api/patients/<id>/` | Retrieve a patient                              |
| PUT    | `/api/patients/<id>/` | Update a patient                                |
| DELETE | `/api/patients/<id>/` | Delete a patient                                |

Users can only access patients they created.

## Doctor APIs

All doctor endpoints require authentication.

| Method | Endpoint             | Description       |
| ------ | -------------------- | ----------------- |
| POST   | `/api/doctors/`      | Create a doctor   |
| GET    | `/api/doctors/`      | List doctors      |
| GET    | `/api/doctors/<id>/` | Retrieve a doctor |
| PUT    | `/api/doctors/<id>/` | Update a doctor   |
| DELETE | `/api/doctors/<id>/` | Delete a doctor   |

## Patient–Doctor Mapping APIs

All mapping endpoints require authentication.

| Method | Endpoint                      | Description                       |
| ------ | ----------------------------- | --------------------------------- |
| POST   | `/api/mappings/`              | Assign a doctor to a patient      |
| GET    | `/api/mappings/`              | List patient–doctor mappings      |
| GET    | `/api/mappings/<patient_id>/` | Get doctors assigned to a patient |
| DELETE | `/api/mappings/<id>/`         | Remove a patient–doctor mapping   |

Duplicate patient–doctor assignments are prevented.

## Error Handling

The API validates request data and handles common errors such as:

* Missing required fields
* Invalid email addresses
* Invalid passwords
* Duplicate email addresses
* Invalid patient or doctor IDs
* Duplicate mappings
* Unauthenticated requests
* Invalid JWT tokens
* Nonexistent resources
* Malformed request bodies

Common HTTP status codes include:

```text
400 Bad Request
401 Unauthorized
404 Not Found
```

## Testing

The API can be tested using Postman.

The Postman collection is included in:

```text
postman/Healthcare Backend.postman_collection.json
```

The collection covers:

* Authentication
* Patient CRUD
* Doctor CRUD
* Patient–doctor mappings
* Authentication and validation scenarios

## Development

Run Django's system check:

```bash
python manage.py check
```

Run the development server:

```bash
python manage.py runserver
```

## Environment Variables

The project uses environment variables for sensitive configuration.

The following file is provided as a template:

```text
.env.example
```

The actual `.env` file should remain local and must not be committed to the repository.
