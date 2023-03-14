from pydantic import BaseModel, Field

class HiredEmployees(BaseModel):
    id: int
    name: str = Field(min_length=3)
    datetime: str = Field(min_length=21)
    department_id: int = Field(min_length=1)
    job_id: int = Field(min_length=1)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Harold Vogt",
                "datime": "2021-11-07T02:48:42Z",
                "department_id": "2",
                "job_id": "96"
            }
        }