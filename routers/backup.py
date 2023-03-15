from fastapi import APIRouter
from schemas.schemas_tables import DepartmentsCreate, JobsCreate, HiredEmployeesCreate
from schemas.backup import BackupRequest, RestoreRequest
from config.database import SessionLocal
from services.backup import Backup
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

backup_router = APIRouter()

@backup_router.post('/backup', tags=['backup-restore'], response_model=dict, status_code=201)
def create_backup_db(backup: BackupRequest) -> dict:
    db = SessionLocal()
    Backup(db).backup_table(backup)
    return JSONResponse(status_code=201, content={"message": "Backup finished"})

@backup_router.post('/restore', tags=['backup-restore'], response_model=dict, status_code=201)
def create_restore_db(restore: RestoreRequest) -> dict:
    db = SessionLocal()
    Backup(db).restore_table(restore)
    return JSONResponse(status_code=201, content={"message": "Restore finished"})