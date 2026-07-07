# FastAPI CRUD Application with JWT Authentication

## 📌 Project Overview

This project is a RESTful CRUD (Create, Read, Update, Delete) API built using **FastAPI**. It implements **JWT (JSON Web Token) Authentication** to secure protected APIs and uses **bcrypt** for password hashing.

The application allows users to register, log in, and perform CRUD operations after successful authentication.

This project was developed as part of my **Choice TechLab Internship** to gain hands-on experience in backend development using FastAPI.

---

## 🚀 Features

- ✅ User Registration
- ✅ User Login
- ✅ JWT Authentication
- ✅ Password Hashing using bcrypt
- ✅ Protected CRUD APIs
- ✅ Duplicate Email Validation
- ✅ Partial User Update
- ✅ MySQL Database Integration
- ✅ SQLAlchemy ORM
- ✅ Environment Variables using `.env`
- ✅ Proper HTTP Status Codes & Exception Handling

---

## 🛠️ Technologies Used

- Python
- FastAPI
- SQLAlchemy
- MySQL
- JWT (python-jose)
- bcrypt
- Pydantic
- python-dotenv
- Uvicorn

---

## 📂 Project Structure

```
01_CRUD_Application
│
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   └── main.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
│
├── database.sql
├── database connection flow.png
├── FastAPI Crud application.png
├── FastAPI internal working.png
├── Overall crud operation.png
└── postman workflow.png
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-github-username>/fastapi-crud-application.git
```

### 2. Navigate to the project directory

```bash
cd 01_CRUD_Application
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
```

> **Note:** Never upload your actual `.env` file to GitHub.

---

## 🗄️ Database Configuration

This project uses **MySQL** as the database.

Update your database connection in `app/database.py` according to your MySQL configuration.

Example:

```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/database_name"
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📮 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT |
| GET | `/users/{user_id}` | Get user details (Protected) |
| POST | `/users/{user_id}` | Update user details (Protected) |
| DELETE | `/users/{user_id}` | Delete user (Protected) |

---

## 🔐 Authentication Flow

1. Register a new user.
2. Login using email and password.
3. Receive a JWT Access Token.
4. Copy the Access Token.
5. Add it to the Authorization header:

```
Authorization: Bearer <your_access_token>
```

6. Access protected APIs.

---

## 📚 Concepts Implemented

- FastAPI Routing
- Dependency Injection (`Depends`)
- JWT Authentication
- OAuth2PasswordBearer
- Password Hashing (bcrypt)
- SQLAlchemy ORM
- MySQL Database Connectivity
- Pydantic Models
- Environment Variables
- CRUD Operations
- Exception Handling
- HTTP Status Codes

---

## 📷 Project Documentation

The repository also contains workflow diagrams for better understanding:

- Database Connection Flow
- FastAPI CRUD Application Flow
- FastAPI Internal Working
- Overall CRUD Operation Flow
- Postman Workflow

---

## 👩‍💻 Author

**Sayali Patil**

Developed as part of the **Choice TechLab Internship** to learn Backend Development using FastAPI, SQLAlchemy, JWT Authentication, and MySQL.

---

## 📄 License

This project is developed for learning and internship purposes.