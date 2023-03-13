from google.cloud import secretmanager
import json

def load_credentials(name_secret):
    # ID Secret
    project_id = "code-challenge-de-380423"
    secret_id = f"projects/{project_id}/secrets/{name_secret}/versions/latest"

    client = secretmanager.SecretManagerServiceClient()

    response = client.access_secret_version(request={"name": secret_id})

    payload = response.payload.data.decode("UTF-8")

    cred = json.loads(payload)

    return cred
