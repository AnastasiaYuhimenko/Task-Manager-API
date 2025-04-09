from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, TaskOut, TaskUpdate
from app.auth.jwt_user import get_current_user
from app.db.database import SessionLocal
from app.crud import task_crud
from app.models.user import User
from typing import List

router = APIRouter(prefix="/task", tags=["tasks"])


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[TaskOut])
def get_user_tasks(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return task_crud.get_task(user_id=current_user.id, db=db)


@router.post("/", response_model=TaskCreate)
def create_user_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return task_crud.create_task(db=db, task=task, user_id=current_user.id)


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = task_crud.delete_task(db=db, task_id=task_id, user_id=current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return {"message": "Задача удалена!"}


@router.put("/{task_id}")
def uptade_task(
    task_index: int,
    updated: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = task_crud.update_task(
        db=db,
        task_id=task_index,
        user_id=current_user.id,
        data=updated.dict(exclude_unset=True),
    )

    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    return task
