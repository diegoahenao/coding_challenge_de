from utils.read_secret import load_credentials
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

USER = load_credentials("code_challenge_db_password")["user"]
PASSWORD = load_credentials("code_challenge_db_password")["password"]
DB_NAME = load_credentials("code_challenge_db_password")["db_name"]
HOST = "127.0.0.1"
PORT = "5432"

DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
engine = create_engine(DATABASE_URL, echo=True)
engine_db = create_engine(DATABASE_URL, echo=True).connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()