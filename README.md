# 🚀 Django Internship Assignment

A Django project showcasing REST API development, authentication, background task handling with Celery, and Telegram bot integration — built with production-ready practices.

---

## ✨ Features

- 🔗 Django REST Framework with public and protected API endpoints  
- 🔒 Token-based authentication (via DRF or JWT)  
- 📧 Celery tasks (e.g., email sending) with Redis as broker  
- 🤖 Telegram Bot that captures user `/start` command and stores their username  
- ⚙️ Environment-based settings with `DEBUG=False` for production setup  
- 📁 Clean code structure and version control  

---

## ✅ Requirements

- Python 3.8+
- PostgreSQL
- Redis
- Telegram Bot Token (Get from [BotFather](https://t.me/BotFather))

---

## 🛠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Manjunath4518/django-internship-assignment.git
cd django-internship-assignment
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

- Copy `.env.example` and rename it to `.env`  
- Fill in the required details like `SECRET_KEY`, `DB_NAME`, `TELEGRAM_BOT_TOKEN`, etc.

```bash
cp .env.example .env
```

### 5. Set up the database

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

---

## ⚙️ Start Celery and Redis

### 1. Start Redis server (make sure it's running)

```bash
redis-server
```

### 2. Start Celery worker

```bash
celery -A project_name worker --loglevel=info
```

> Replace `project_name` with your actual Django project name.

---

## 🤖 Telegram Bot Setup

1. Create a bot on Telegram using [@BotFather](https://t.me/BotFather).  
2. Get the bot token and add it to your `.env`.  
3. Run the Telegram bot listener (script should handle message parsing and saving usernames).

---





## 👨‍💻 Author

**B. Manjunath**  
GitHub: [@Manjunath4518](https://github.com/Manjunath4518)
