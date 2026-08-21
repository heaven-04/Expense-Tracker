# Expense Tracker API

A simple, secure REST API for tracking personal expenses, built with **FastAPI**. Users can create an account, log in, and manage their own expenses through JWT-authenticated endpoints.

## Features

- **User authentication** – sign up and log in with email/password
- **Secure password storage** – passwords are hashed with `pwdlib`, never stored in plain text
- **JWT-based authorization** – protected routes require a valid Bearer token
- **Expense management** – create, view, and delete expenses tied to the logged-in user
- **Data isolation** – users can only view and delete their own expenses
- **Auto-generated API docs** – interactive Swagger UI out of the box (courtesy of FastAPI)

## Tech Stack

| Layer          | Technology |
|----------------|------------|
| Framework      | [FastAPI](https://fastapi.tiangolo.com/) |
| ORM            | [SQLAlchemy](https://www.sqlalchemy.org/) |
| Database       | PostgreSQL (configurable via connection URL) |
| Validation     | [Pydantic](https://docs.pydantic.dev/) |
| Authentication | OAuth2 + [JWT](https://python-jose.readthedocs.io/) (`python-jose`) |
| Password Hashing | [pwdlib](https://frankie567.github.io/pwdlib/) |
| Server         | [Uvicorn](https://www.uvicorn.org/) |

## Project Structure

```
Expense-Tracker/
├── APP/
│   ├── main.py        # FastAPI app entry point
│   ├── oauth2.py       # JWT creation & verification
│   └── utils.py        # Password hashing helpers
├── Database/
│   └── database.py     # SQLAlchemy engine & session setup
├── models/
│   └── models.py       # SQLAlchemy ORM models (User, Expense)
├── Routes/
│   ├── auth.py          # /login and /signup endpoints
│   └── expenses.py      # /expenses endpoints (CRUD)
├── schemas/
│   └── schemas.py       # Pydantic request/response schemas
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.11+
- A running PostgreSQL instance

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/heaven-04/Expense-Tracker.git
   cd Expense-Tracker
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose pwdlib[argon2] pydantic[email] python-multipart
   ```

4. Configure your database connection in `Database/database.py`:
   ```python
   SQLALCHEMY_DATABASE_URL = "postgresql://<user>:<password>@<host>/<dbname>"
   ```

5. Run the application
   ```bash
   uvicorn APP.main:app --reload
   ```

6. Open your browser to `http://127.0.0.1:8000/docs` to explore the interactive API documentation.

## API Endpoints

### Authentication

| Method | Endpoint   | Description                    |
|--------|------------|---------------------------------|
| POST   | `/signup`  | Create a new user account       |
| POST   | `/login`   | Log in and receive a JWT token  |

### Expenses (require Bearer token)

| Method | Endpoint                | Description                          |
|--------|--------------------------|---------------------------------------|
| GET    | `/expenses/`             | Get all expenses for the current user |
| POST   | `/expenses/add`          | Add a new expense                     |
| DELETE | `/expenses/delete/{id}`  | Delete an expense by ID               |


