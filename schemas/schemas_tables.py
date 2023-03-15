from pydantic import BaseModel, Field

class DepartmentsCreate(BaseModel):
    id: int
    department: str = Field(min_length=2)

class JobsCreate(BaseModel):
    id: int
    job: str = Field(min_length=2)

class HiredEmployeesCreate(BaseModel):
    id: int
    name: str = Field(min_length=3)
    datetime: str = Field(min_length=19)
    department_id: int
    job_id: int