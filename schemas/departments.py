from pydantic import BaseModel, Field

class Departments(BaseModel):
    id: int
    department: str = Field(min_length=2)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "department": "Product Management"
            }
        }