from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Departments(Base):

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String, index=True)
    hired_employees = relationship("HiredEmployees", back_populates="departments")
