from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class HiredEmployees(Base):

    __tablename__ = "hired_employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    datetime = Column(String, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    departments = relationship("Department", back_populates="hired_employees")
    job_id = Column(Integer, ForeignKey("jobs.id"))
    jobs =relationship("Job", back_populates="hired_employees")