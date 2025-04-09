from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate
from fastapi import HTTPException


def get_task(db: Session, user_id: int):
    return db.query(Task).filter(Task.owner_id == user_id).all()


def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int, user_id: int):
    task = db.query(Task).filter(Task.owner_id == user_id, Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найден")

    db.delete(task)
    db.commit()
    return task


def update_task(db: Session, task_id: int, user_id: int, data: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    allowed_fields = ["title", "description", "is_completed"]

    for key, value in data.items():
        if key in allowed_fields:
            if hasattr(task, key):
                setattr(task, key, value)
            else:
                raise HTTPException(
                    status_code=400, detail=f"Поле {key} не существует в модели Task"
                )
        else:
            raise HTTPException(
                status_code=400, detail=f"Поле {key} не существует в модели Task"
            )

    db.commit()
    db.refresh(task)
    return task
