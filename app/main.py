from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import User
from db import SessionLocal, engine, Base 
from schemas import UserCreate, UserRead
from typing import List

app = FastAPI()

# создаём таблицы
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "It works!"}

# зависимость для получения сессии
def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/users")
def create_user(user: dict, database: Session = Depends(get_db)):
    new_user = User(name=user["name"], email=user["email"])  # без models.
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return {"message": "User created", "id": new_user.id}

@app.get("/users")
def get_users(database: Session = Depends(get_db)):
    users = database.query(User).all()  # без models.
    return {"users": users}
