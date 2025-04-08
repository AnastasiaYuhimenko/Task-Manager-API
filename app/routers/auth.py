from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserOut
from app.crud.user_crud import create_user, get_user_by_email
from app.db.database import SessionLocal


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
