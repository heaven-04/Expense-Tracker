from fastapi import FastAPI
from Routes import auth ,expenses
from models import models
from Database.database import engine
models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Expense Tracker" , description="simple expense tracker application to manage your finances")

app.include_router(auth.router)
app.include_router(expenses.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
