import requests
import json


class Domains:
    transip_base_url='https://api.transip.nl/v6/domains'
    def __init__(self, headers):
        self.headers = headers

    def get(self):
        res = requests.get(self.transip_base_url, headers=self.headers)
        if res.status_code != 200:
            print('Getting domains failed with status code: ' + str(res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def get_dns(self, domain):
        url=self.transip_base_url + '/' + domain + '/dns'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Getting dns entries failed with status code: ' + str(res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def post_dns(self, domain, data):
        url = self.transip_base_url + '/' + domain + '/dns'
        res = requests.post(url, headers=self.headers, data=data)
        if res.status_code != 201:
            print('Creating dns entry failed with status code: ' + str(res.status_code))
            print(res.text)
            exit(1)
        return

    def patch_dns(self, domain, data):
        url = self.transip_base_url + '/' + domain + '/dns'
        res = requests.patch(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Changing dns entry failed with status code: ' + str(res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return
