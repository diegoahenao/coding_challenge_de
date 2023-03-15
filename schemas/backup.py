from pydantic import BaseModel, Field

class BackupRequest(BaseModel):
    table_name: str = Field(min_length=2)

class RestoreRequest(BaseModel):
    table_name: str = Field(min_length=2)
    file_name: str = Field(min_length=5)