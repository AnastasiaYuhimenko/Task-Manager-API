from fastapi import APIRouter, Depends
from app.auth.jwt_user import get_current_user
from app.schemas.user_schema import UserOut
from app.models.user import User


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
