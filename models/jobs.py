from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Jobs(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job = Column(String, index=True)
    hired_employees = relationship("HiredEmployees", back_populates="jobs")