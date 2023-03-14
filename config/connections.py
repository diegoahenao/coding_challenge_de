from utils.read_secret import load_credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.cloud import storage
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
BUCKET_NAME = "code-challenge-de"
FOLDER_ID = "1h4fmPDkEzTMRGe6QXXTcMBE-oA1K656k"

# Create an API PyDrive instance
credentials_gdrive = service_account.Credentials.from_service_account_info(load_credentials("code_challenge_secret"), scopes=SCOPES)
drive_service = build("drive", "v3", credentials=credentials_gdrive)

# Create API Storage instance
credentials = service_account.Credentials.from_service_account_info(load_credentials("code_challenge_secret"))
client_storage = storage.Client(credentials=credentials)

# Create connection with PostgreSQL in Cloud SQL
db_user = load_credentials("code_challenge_db_password")["user"]
db_password = load_credentials("code_challenge_db_password")["password"]
db_name = load_credentials("code_challenge_db_password")["db_name"]
db_host = "127.0.0.1"
db_port = "5432"

database_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()





