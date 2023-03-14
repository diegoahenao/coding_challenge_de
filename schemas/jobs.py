from pydantic import BaseModel, Field

class Jobs(BaseModel):
    id: int
    job: str = Field(min_length=2)