from config.connections import Base
from sqlalchemy import Column, Integer, String

class jobs(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    job = Column(String)