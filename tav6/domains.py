import requests

transip_base_url='https://api.transip.nl/v6/domains'

def get(headers):
    return requests.get(transip_base_url, headers=headers).text
