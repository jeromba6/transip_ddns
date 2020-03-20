#!/usr/bin/env python3
import requests
import json
import transipApiV6
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--login',  required=True, dest='login',   help='Login name for Transip')
parser.add_argument('-d', '--domain', required=True, dest='domain',  help='Domain under which the entry should be controlled')
parser.add_argument('-e', '--entry',  required=True, dest='entry',   help='Entry under the domain which should be used to store the ip')
parser.add_argument('-i', '--ip',                    dest='ip',      help='IP adress to store in the given entry')
group = parser.add_mutually_exclusive_group()
group.add_argument('-k', '--key',     dest='key',     help='API key to autenticate at Transip')
group.add_argument('-f', '--keyfile', dest='keyfile', help='API key stored in file to autenticate at Transip')

arg_results = parser.parse_args()

if not isinstance(arg_results.key, str) and not isinstance(arg_results.keyfile, str):
  print('There shou be an argument for -f/--keyfile or -k/--key')
  exit(1)

# Get public IP if not set
if isinstance(arg_results.ip, str):
  pub_ip = arg_results.ip
else:
  res = requests.get('https://ipinfo.io')
  if res.status_code != 200:
      print('Failed to get public ip.')
      exit(1)
  pub_ip=json.loads(res.text)['ip']

# Get key for transip
if isinstance(arg_results.keyfile, str):
  key_file = open(arg_results.keyfile, "r")
  key = key_file.read()
  key_file.close()
else:
  key = arg_results.key

# Get Header for authentication against transip api V6
headers = transipApiV6.Generic(arg_results.login, key).get_headers()

# Request domains managed by this account
domains=transipApiV6.Domains(headers)

# Request DNS entries for this domain
dns_entries = domains.list_dns_entries(arg_results.domain)

# Find entry
found_dns_entries = []
for dns_entry in dns_entries['dnsEntries']:
  if dns_entry['name'] == arg_results.entry and dns_entry['type'] == 'A':
    found_dns_entries.append(dns_entry)

# Change entry for this domain with current public IP
if len(found_dns_entries) == 0:
  data = '''{
    "dnsEntry": {
      "name": "''' + arg_results.entry + '''",
      "expire": 300,
      "type": "A",
      "content": "''' + pub_ip + '''"
    }
  }
  '''
  domains.add_dns_entry(arg_results.domain, data)
  print('New entry created for {0}.{1} with ip {2}'.format(arg_results.entry, arg_results.domain, pub_ip))
elif len(found_dns_entries) == 1:
  if found_dns_entries[0]['content'] == pub_ip:
    print('No change needed')
  else:
    print('Change dns entry')
    print('From: {0}'.format(json.dumps(found_dns_entries[0])))
    found_dns_entries[0]['content'] = pub_ip
    print('To  : {0}'.format(json.dumps(found_dns_entries[0])))
    domains.update_dns_entry(arg_results.domain, '{"dnsEntry": ' + json.dumps(found_dns_entries[0]) +'}')
else:
  print('Multiple entries found, can\'t determine which to change (if any).')
