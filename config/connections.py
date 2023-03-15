from utils.read_secret import load_credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.cloud import storage

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
BUCKET_NAME = "code-challenge-de"
FOLDER_ID = "1h4fmPDkEzTMRGe6QXXTcMBE-oA1K656k"
EMAIL_AUTH = load_credentials("code_challenge_auth")["user"]
PASS_AUTH = load_credentials("code_challenge_auth")["password"]

# Create an API PyDrive instance
credentials_gdrive = service_account.Credentials.from_service_account_file('./credentials/credentials.json', scopes=SCOPES)
drive_service = build("drive", "v3", credentials=credentials_gdrive)

# Create API Storage instance
credentials = service_account.Credentials.from_service_account_file('./credentials/credentials.json')
client_storage = storage.Client(credentials=credentials)