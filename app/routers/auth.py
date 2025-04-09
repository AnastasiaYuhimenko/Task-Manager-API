from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserOut
from app.crud.user_crud import create_user, get_user_by_email
from app.schemas.token_schema import Token
from app.db.database import SessionLocal
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import User
from app.auth.hash import verify_password
from app.auth.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserOut, status_code=200)
def register(user: UserCreate, db: Session = Depends(get_db)):
    user_exist = get_user_by_email(email=user.email, username=user.username, db=db)
    if user_exist:
        raise HTTPException(
            status_code=400, detail="Такой пользователь уже существует :("
        )
    return create_user(db=db, user=user)


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = (
        db.query(User).filter(User.email == form_data.username).first()
    )  #  юзаем email как username, так надо)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не зарегистрирован")

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Неверный пароль")

    token = create_access_token(
        data={"sub": user.email}
    )  #  sub = subject; sub — это стандарт в JWT
    return {"access_token": token, "token_type": "bearer"}
