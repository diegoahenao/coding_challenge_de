from utils.read_secret import load_credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.cloud import storage

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
BUCKET_NAME = "code-challenge-de"
FOLDER_ID = "1h4fmPDkEzTMRGe6QXXTcMBE-oA1K656k"

# Create an API PyDrive instance
credentials_gdrive = service_account.Credentials.from_service_account_info(load_credentials("code_challenge_secret"), scopes=SCOPES)
drive_service = build("drive", "v3", credentials=credentials_gdrive)

# Create API Storage instance
credentials = service_account.Credentials.from_service_account_info(load_credentials("code_challenge_secret"))
client_storage = storage.Client(credentials=credentials)





