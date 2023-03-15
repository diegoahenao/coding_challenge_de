from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Departments(Base):

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    department = Column(String, index=True)
    hired_employees = relationship("HiredEmployees", back_populates="departments")

class Jobs(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    job = Column(String, index=True)
    hired_employees = relationship("HiredEmployees", back_populates="jobs")

class HiredEmployees(Base):

    __tablename__ = "hired_employees"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, index=True)
    datetime = Column(String, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    departments = relationship("Departments", back_populates="hired_employees")
    job_id = Column(Integer, ForeignKey("jobs.id"))
    jobs =relationship("Jobs", back_populates="hired_employees")

