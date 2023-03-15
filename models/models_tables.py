from config.database import Base
from sqlalchemy import Column, Integer, String

class Departments(Base):

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    department = Column(String, index=True)

class Jobs(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    job = Column(String, index=True)

class HiredEmployees(Base):

    __tablename__ = "hired_employees"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, index=True)
    datetime = Column(String, index=True)
    department_id = Column(Integer)
    job_id = Column(Integer)

