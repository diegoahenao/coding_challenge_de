from io import BytesIO
from schemas.backup import BackupRequest, RestoreRequest
from config.database import engine_db, engine
import pandas as pd
from config.connections import client_storage, BUCKET_NAME
import datetime
from sqlalchemy import text
import pandavro as pdx
import os
import fastavro

class Backup():

    def __init__(self, db) -> None:
        self.db = db

    def backup_table(self, request: BackupRequest):
        table_name = request.table_name
        df = pd.read_sql_table(table_name, engine_db)
        print(df)

        avro_file = table_name + '.avro'
        pdx.to_avro(avro_file, df)
        bucket = client_storage.get_bucket(BUCKET_NAME)
        today_str = datetime.date.today().strftime('%Y-%m-%d')
        today_date = datetime.datetime.strptime(today_str, '%Y-%m-%d').date()
        destination_blob_name = table_name + '/' + table_name + '_' + str(today_date) + '.avro'
        blob = bucket.blob(destination_blob_name)

        with open(avro_file, 'rb') as local_file:
            print(local_file)
            blob.upload_from_file(local_file, content_type='application/octet-stream')
        os.remove(avro_file)


    def restore_table(self, request: RestoreRequest):
        bucket = client_storage.get_bucket(BUCKET_NAME)
        table_name = request.table_name
        file_name = request.file_name
        file_path = table_name + '/' + file_name
        print(file_path)
        blob = bucket.blob(file_path)
        buffer = BytesIO()
        blob.download_to_file(buffer)
        buffer.seek(0)
        avro_reader = fastavro.reader(buffer)
        df = pd.DataFrame.from_records(avro_reader)
        self.db.query(table_name).delete()
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        self.db.commit()
        self.db.close()

