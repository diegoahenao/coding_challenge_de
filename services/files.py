from config.connections import drive_service, client_storage, engine, BUCKET_NAME, FOLDER_ID
import os
import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

class Files():

    def __init__(self, drive_service) -> None:
        self.drive_service = drive_service
    
    def save_files(self):
        query = f"'{FOLDER_ID}' in parents and trashed = false"
        results = self.drive_service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
        files = results.get("files", [])
        if not files:
            return "Files not found"
        else:
            csv_files = [f for f in files if os.path.splitext(f["name"])[1].lower() == ".csv"]
            file_names = []
            for file in csv_files:
                file_id = file["id"]
                file_name = file["name"]
                file_names.append(file_name)
                request = drive_service.files().get_media(fileId=file_id)
                file_content = request.execute()
                bucket = client_storage.bucket(BUCKET_NAME)
                blob = bucket.blob(file_name)
                blob.upload_from_string(file_content)
            return file_names
    
    def load_csv_to_postgres(self, file_names):
        for file_name in file_names:
            with client_storage.bucket(BUCKET_NAME).blob(file_name).open('r') as f:
                table_name = file_name.replace('.csv', '')
                conn = engine.connect()
                result = conn.execute(text(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}' ORDER BY ordinal_position")).fetchall()
                columns = [row[0] for row in result]
                df = pd.read_csv(f, header=None, names=columns)
                try:
                    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
                    print(f"{file_name} loaded to database")
                except IntegrityError as e:
                    print(f"Skipped {file_name}: {e.args[0]}")
                    continue
        return "Files loaded to database"


        
    

