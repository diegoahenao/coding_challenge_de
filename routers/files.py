from fastapi import APIRouter, Depends
from services.files import Files
from config.connections import drive_service
from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer

files_router = APIRouter()

@files_router.post('/files', tags=["files"], response_model = dict, status_code=201, dependencies=[Depends(JWTBearer())])
def get_and_load_files():
    files = Files(drive_service)
    file_names = files.save_files()
    files.load_csv_to_postgres(file_names)
    return JSONResponse(status_code=201, content={"message": "Files were saved and loaded"})

