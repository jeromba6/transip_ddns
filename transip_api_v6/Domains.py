import requests
import json

transip_base_url='https://api.transip.nl/v6/domains'

class Domains:
    def get(headers):
        res = requests.get(transip_base_url, headers=headers)
        if res.status_code != 200:
            print('Getting domains failed with status code: ' + str(res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def get_dns(headers, domain):
        url=transip_base_url + '/' + domain + '/dns'
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print('Getting dns entries failed with status code: ' + str(res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def post_dns(headers, domain, data):
        url = transip_base_url + '/' + domain + '/dns'
        res = requests.post(url, headers=headers, data=data)
        if res.status_code != 201:
            print('Creating dns entry failed with status code: ' + str(res.status_code))
            print(res.text)
            exit(1)
        return

    def patch_dns(headers, domain, data):
        url = transip_base_url + '/' + domain + '/dns'
        res = requests.patch(url, headers=headers, data=data)
        if res.status_code != 204:
            print('Changing dns entry failed with status code: ' + str(res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return
