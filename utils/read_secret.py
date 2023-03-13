from google.cloud import secretmanager
import json

def load_credentials(name_secret):
    # GCP project in which secret is stored
    project_id = "papyrus-data"

    # ID Secret
    secret_id = f"projects/224992036374/secrets/{name_secret}/versions/latest"

    client = secretmanager.SecretManagerServiceClient()

    response = client.access_secret_version(request={"name": secret_id})
    
    payload = response.payload.data.decode("UTF-8")

    cred = json.loads(payload)

    return cred
