from pydantic import BaseModel, Field

class HiredEmployees(BaseModel):
    id: int
    name: str = Field(min_length=3)
    datetime: str = Field(min_length=21)
    department_id: int = Field(min_length=1)
    job_id: int = Field(min_length=1)