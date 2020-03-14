#!/usr/bin/env python3

import requests
import json
import transip_api_v6_bla as transip_api_v6

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

jwt = transip_api_v6.get_jwt('jvgemert', key)

# Create header with JWT
headers = transip_api_v6.get_header(jwt)

# Request domains managed by this account
url='https://api.transip.nl/v6/domains'
# res = json.loads(requests.get(url, headers=headers).text)
# print(json.dumps(transip_api_v6.get_domains,indent=2))
print(json.dumps(json.loads(transip_api_v6.get_domains(jwt)),indent=2))
print()
# Request DNS entries for this domain
url='https://api.transip.nl/v6/domains/gemert.net/dns'
res = json.loads(requests.get(url, headers=headers).text)
print(json.dumps(res,indent=2))
print()

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