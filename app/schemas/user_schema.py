from pydantic import BaseModel, EmailStr, field_validator
import re


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

    @field_validator("password")
    def password_must_be_strong(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"\d", value):  # Проверка на наличие хотя бы одной цифры
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[A-Za-z]", value):  # Проверка на наличие хотя бы одной буквы
            raise ValueError("Password must contain at least one letter")
        return value


class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        orm_mode = True
