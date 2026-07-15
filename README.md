# Personal Markdown Notes API

## Опис проєкту

Personal Markdown Notes API — це REST API для створення персональних нотаток у форматі Markdown.

Користувач може зареєструватися, авторизуватися, створювати нотатки, переглядати список нотаток, шукати їх за тегами, видаляти нотатки та конвертувати Markdown у HTML.

## Використані технології

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Markdown
- Uvicorn
- systemd
- GitHub

## Використані AWS-сервіси

- EC2 — сервер для запуску FastAPI-додатку
- Security Groups — налаштування доступу до портів 22 та 8000

## API endpoints

- POST /auth/register — реєстрація користувача
- POST /auth/login — авторизація користувача
- POST /notes/ — створення нотатки
- GET /notes/ — список нотаток
- GET /notes/?tag=aws — пошук за тегом
- GET /notes/{note_id} — перегляд нотатки
- GET /notes/{note_id}/html — конвертація Markdown у HTML
- DELETE /notes/{note_id} — видалення нотатки

## Environment variables

На сервері використовується .env файл:

```env
DATABASE_URL=postgresql://notes_user:notes_password_123@localhost:5432/notes_db
SECRET_KEY= ="Ваш ключ"
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
