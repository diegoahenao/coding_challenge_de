from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.files import files_router
from routers.tables import tables_router
from config.database import Base, engine
from models.models_tables import Departments, Jobs, HiredEmployees
from routers.backup import backup_router
from routers.user import user_router
from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.title = "Code Challenge Data Engineer"
app.version = "0.0.1"

# Routers
app.add_middleware(ErrorHandler)
app.include_router(files_router)
app.include_router(tables_router)
app.include_router(backup_router)
app.include_router(user_router)

# Create Tables
Base.metadata.create_all(bind=engine)

# API path
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>API Online</h1>')