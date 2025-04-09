from fastapi import FastAPI
from app.routers import auth
from app.routers import user
from app.routers import task

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello all world!"}


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(task.router)
