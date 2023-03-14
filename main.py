from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.files import files_router
from config.database import Base, engine
from models.hired_employees import Hired_employees
from models.departments import Departments
from models.jobs import Jobs
import logging

app = FastAPI()
app.title = "Code Challenge Data Engineer"
app.version = "0.0.1"

# Routers
app.include_router(files_router)

# Create Tables
Base.metadata.create_all(bind=engine)

# API path
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>API Online</h1>')