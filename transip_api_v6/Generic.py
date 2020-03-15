from OpenSSL import crypto
import base64
import requests
import random
import string
import json

def randomDigits(self, stringLength=10):
    """Generate a random string of letters and digits """
    return ''.join(random.choice(string.digits) for i in range(stringLength))

class Generic:
    base_url='https://api.transip.nl/v6/auth'
    def __init__(self, login, key):
        self.login = login
        self.key = key

    def get_jwt(self):
        pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, self.key)
        data = '{ "login": "' + self.login + '", "nonce": ' + randomDigits(10) + ' }'
        signature = base64.b64encode(crypto.sign(pkey, data.encode(), "sha512")).decode()
        headers = {'Signature': signature, 'Accept': 'application/json'}
        res = requests.post(self.base_url, headers=headers, data=data.encode())
        if res.status_code != 201:
            print('Could not create a JWT. Status_code was: ' + str(res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)['token']

    def get_headers(self):
       return {'Authorization': 'Bearer ' + Generic.get_jwt(self), 'Accept': 'application/json'}
