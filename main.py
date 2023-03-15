from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.files import files_router
from routers.tables import tables_router
from config.database import Base, engine
from models.models_tables import Departments, Jobs, HiredEmployees

app = FastAPI()
app.title = "Code Challenge Data Engineer"
app.version = "0.0.1"

# Routers
app.include_router(files_router)
app.include_router(tables_router)

# Create Tables
Base.metadata.create_all(bind=engine)

# API path
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>API Online</h1>')