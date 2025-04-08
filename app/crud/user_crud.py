from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)


#  Регистрация пользователя
def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)

    db_user = User(
        email=user.email, username=user.username, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # обновляем состояние объекта
    return db_user


#  для проверки существования пользователя
def get_user_by_email(db: Session, email: str, username: str):
    """Проверка на то, существует ли такой пользователь"""
    return (
        db.query(User).filter(User.email == email or User.username == username).first()
    )
