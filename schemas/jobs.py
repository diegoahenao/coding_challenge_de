from pydantic import BaseModel, Field

class Jobs(BaseModel):
    id: int
    job: str = Field(min_length=2)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "job": "Marketing Assistant"
            }
        }