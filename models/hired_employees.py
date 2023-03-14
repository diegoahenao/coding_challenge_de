from config.connections import Base
from sqlalchemy import Column, Integer, String

class hired_employees(Base):

    __tablename__ = "hired_amployees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    datetime = Column(String)
    department_id = Column(String)
    job_id = Column(Integer)