# 📝 Task Manager API

**Task Manager API** — это backend-сервис, построенный на FastAPI, который позволяет пользователям регистрироваться, авторизовываться и управлять личными задачами (создание, редактирование, удаление, просмотр). Все действия с задачами защищены JWT-токеном.

---

## 🚀 Технологии

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Docker & Docker Compose](https://docs.docker.com/)
- [JWT Authentication](https://jwt.io/)
- [Passlib (bcrypt)](https://passlib.readthedocs.io/en/stable/)

---

## 📦 Возможности

- Регистрация пользователей
- Авторизация по email и паролю
- Получение JWT-токена
- Защищённые эндпоинты
- CRUD для задач:
  - Создание задачи
  - Обновление задачи
  - Удаление задачи
  - Получение списка задач только текущего пользователя
- Валидация данных через Pydantic

---

## 🧱 Структура проекта

app/ 
  ├── auth/ # авторизация и безопасность (JWT, хеши)
  ├── crud/ # логика работы с БД 
  ├── db/ # подключение к базе данных 
  ├── models/ # SQLAlchemy модели 
  ├── routers/ # FastAPI роуты 
  ├── schemas/ # схемы Pydantic (валидация данных) 
  ├── main.py # точка входа

Если честно, README не я писала, мне было лень))
