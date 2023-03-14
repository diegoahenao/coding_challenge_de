from pydantic import BaseModel, Field

class Departments(BaseModel):
    id: int
    department: str = Field(min_length=2)