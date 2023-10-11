import os
import requests
import pandas as pd
from dotenv import load_dotenv
from google.cloud import storage

def get_google_client(environment):
    if environment == 'local':
        return storage.Client()
    else :
        return storage.Client.from_service_account_json(os.getenv('creds_json_path'))

load_dotenv()
env = os.getenv('ENV') or 'local'

req_headers = {
    'User-Agent': '19rithik@gmail.com'
}

tickers_req = requests.get('https://www.sec.gov/files/company_tickers.json', headers = req_headers)

json_data = tickers_req.json()

gclient = get_google_client(env)
print(list(gclient.list_buckets()))