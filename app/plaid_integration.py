import requests

PLAID_CLIENT_ID = "your_client_id"
PLAID_SECRET = "your_secret"

def get_bank_transactions():
    url = "https://sandbox.plaid.com/transactions/get"
    headers = {"Content-Type": "application/json"}
    payload = {
        "client_id": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
        "access_token": "your_access_token"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
