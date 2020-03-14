#!/usr/bin/env python3

from OpenSSL import crypto
import base64
import requests
import random
import string
import json

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# Get public IP
res = requests.get('https://ipinfo.io')
if res.status_code != 200:
    print('Failed to get public ip.')
    exit()
pub_ip=json.loads(res.text)['ip']

# Get JWT for authentication against transip api V6
key_file = open("test copy.pem", "r")
key = key_file.read()
key_file.close()
pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
data = '{ "login": "jvgemert", "nonce": ' + randomStringDigits(10)+ ' }'
sign = crypto.sign(pkey, data.encode(), "sha512")
data_base64 = base64.b64encode(sign)
headers = {'Signature': data_base64.decode(), 'Accept': 'application/json' }
url='https://api.transip.nl/v6/auth'
res = requests.post(url, headers=headers, data=data)
if res.status_code != 201:
    print('Could not create a JWT status_code was:' + str(res.status_code))
    exit()
jwt=json.loads(res.text)['token']

# Create header with JWT
headers = {'Authorization': 'Bearer ' + jwt, 'Accept': 'application/json'}

# Request domains managed by this account
url='https://api.transip.nl/v6/domains'
res = json.loads(requests.get(url, headers=headers).text)
print(json.dumps(res,indent=2))

# Request DNS entries for this domain
url='https://api.transip.nl/v6/domains/gemert.net/dns'
res = json.loads(requests.get(url, headers=headers).text)
print(json.dumps(res,indent=2))

# Change entry for this domain with current public IP
data = '''{
  "dnsEntry": {
    "name": "test-script",
    "expire": 3600,
    "type": "A",
    "content": "''' + pub_ip + '''"
  }
}
'''

res = requests.patch(url, headers=headers, data=data)
if res.status_code != 204:
    print('Changing dns entry failed with status code: ' + str(res.status_code))
    exit()
print('DNS entry change was succesful')