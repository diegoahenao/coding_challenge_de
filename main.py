from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.files import files_router

app = FastAPI()
app.title = "Code Challenge Data Engineer"
app.version = "0.0.1"

# Routers

app.include_router(files_router)

# API paths

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>API Online</h1>')