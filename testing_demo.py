#!/usr/bin/env python3
import requests
import json
import transip_api_v6

login          = 'jvgemert'
keyfile        = 'test copy.pem'
domain         = 'transipdemonstratie.com'
find_dns_entry = '@'

# Get public IP
res = requests.get('https://ipinfo.io')
if res.status_code != 200:
    print('Failed to get public ip.')
    exit(1)
pub_ip=json.loads(res.text)['ip']

# Get Header for authentication against transip api V6
key_file = open(keyfile, "r")
key = key_file.read()
key_file.close()
# ph = transip_api_v6.Generic(login, key)
headers = transip_api_v6.Generic(login, key, True).get_headers()

# Request domains managed by this account
domains=transip_api_v6.Domains(headers)
managed_domains=domains.list_domains()
print(json.dumps(managed_domains,indent=2))
print()

managed_domains=domains.info_tld('nl')
print(json.dumps(managed_domains,indent=2))
print()
exit()

data = '''{
  "domainNames": [
    "gemert.net"
  ]
}'''
managed_domains=domains.domains_availability(data)
print(json.dumps(managed_domains,indent=2))
print()
exit()
