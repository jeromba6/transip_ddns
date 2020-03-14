from OpenSSL import crypto
import base64
import requests
import random
import string
import json
# import domain

transip_base_url='https://api.transip.nl/v6/'

def randomStringDigits(stringLength=6):
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

def get_header(jwt):
    return {'Authorization': 'Bearer ' + jwt, 'Accept': 'application/json'}

def get_domains(jwt):
    url=transip_base_url+'domains'
    return requests.get(url, headers=get_header(jwt)).text



# # Create header with JWT
# headers = {'Authorization': 'Bearer ' + jwt, 'Accept': 'application/json'}

# # Request domains managed by this account
# url='https://api.transip.nl/v6/domains'
# res = json.loads(requests.get(url, headers=headers).text)
# print(json.dumps(res,indent=2))

# # Request DNS entries for this domain
# url='https://api.transip.nl/v6/domains/gemert.net/dns'
# res = json.loads(requests.get(url, headers=headers).text)
# print(json.dumps(res,indent=2))

# # Change entry for this domain with current public IP
# data = '''{
#   "dnsEntry": {
#     "name": "test-script",
#     "expire": 3600,
#     "type": "A",
#     "content": "''' + pub_ip + '''"
#   }
# }
# '''

# res = requests.patch(url, headers=headers, data=data)
# if res.status_code != 204:
#     print('Changing dns entry failed with status code: ' + str(res.status_code))
#     exit()
# print('DNS entry change was succesful')