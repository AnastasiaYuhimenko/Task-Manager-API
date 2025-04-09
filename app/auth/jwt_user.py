from fastapi import HTTPException, status, Security, Depends
from jose import jwt, JWTError
from app.auth.jwt_bearer import get_token
from app.models.user import User
from app.db.database import SessionLocal
from sqlalchemy.orm import Session
import os

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(get_token), db: Session = Depends(get_db)
) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")  # вот он sub, email
        if email is None:
            raise HTTPException(status_code=404, detail="email не найден")
    except JWTError:
        raise HTTPException(status_code=401, detail="Токен неверный или истек")

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user
