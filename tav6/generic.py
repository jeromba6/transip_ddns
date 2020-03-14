from OpenSSL import crypto
import base64
import requests
import random
import string
import json

transip_base_url='https://api.transip.nl/v6/'

def randomStringDigits(stringLength=10):
    """Generate a random string of letters and digits """
    return ''.join(random.choice(string.digits) for i in range(stringLength))

def get_jwt(login, key):
    url = transip_base_url + 'auth'
    pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
    data = '{ "login": "' + login + '", "nonce": ' + randomStringDigits(10)+ ' }'
    signature = base64.b64encode(crypto.sign(pkey, data.encode(), "sha512")).decode()
    headers = {'Signature': signature, 'Accept': 'application/json'}
    res = requests.post(url, headers=headers, data=data.encode())
    if res.status_code != 201:
        print('Could not create a JWT. Status_code was: ' + str(res.status_code))
        print(res.text)
        exit()
    return json.loads(res.text)['token']

def get_headers(login, key):
    url = transip_base_url + 'auth'
    pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
    data = '{ "login": "' + login + '", "nonce": ' + randomStringDigits(10)+ ' }'
    signature = base64.b64encode(crypto.sign(pkey, data.encode(), "sha512")).decode()
    headers = {'Signature': signature, 'Accept': 'application/json'}
    res = requests.post(url, headers=headers, data=data.encode())
    if res.status_code != 201:
        print('Could not create a JWT. Status_code was: ' + str(res.status_code))
        print(res.text)
        exit()
    return {'Authorization': 'Bearer ' + json.loads(res.text)['token'], 'Accept': 'application/json'}
