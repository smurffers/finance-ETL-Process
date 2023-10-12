import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv
from google.cloud import storage

def get_google_client(environment):
    if environment == 'local':
        return storage.Client()
    else :
        return storage.Client.from_service_account_json(os.getenv('creds_json_path'))

def create_json(json_object, file_name, client):
    bucket = client.get_bucket('stock-companies-id')
    
    #Create a blob
    blob = bucket.blob(file_name)

    # Upload blob
    blob.upload_from_string(
        data = json.dumps(json_object),
        content_type='application/json'
    )

    return 'Upload Successfull'

load_dotenv()
env = os.getenv('ENV') or 'local'

req_headers = {
    'User-Agent': '19rithik@gmail.com'
}

tickers_req = requests.get('https://www.sec.gov/files/company_tickers.json', headers = req_headers)

response = create_json(tickers_req.json(), 'company-tickers.json', get_google_client(env))

print(response)