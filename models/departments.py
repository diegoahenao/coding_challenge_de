from config.connections import Base
from sqlalchemy import Column, Integer, String, Float

class departments(Base):

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    department = Column(String)