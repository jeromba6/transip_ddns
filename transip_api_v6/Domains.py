import requests
import json

class Domains:
    base_url='https://api.transip.nl/v6/domains'
    def __init__(self, headers):
        self.headers = headers

    def list_domains(self):
        url = self.base_url
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Getting domains failed with status code: {0}'.format(res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def retrieve_domain(self, domain):
        url = self.base_url + '/' + domain
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Retrieve domain "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def register_domain(self, data):
        url = self.base_url
        res = requests.post(url, headers=self.headers, data=data)
        if res.status_code != 201:
            print('Creating/Transfering domain failed with status code: {0}'.format(res.status_code))
            print(res.text)
            exit(1)
        return

    def tranfer_domain(self, data):
        return Domains.register_domain(self, data)

    def update_domain(self, data):
        url = self.base_url
        res = requests.put(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Creating/Transfering domain failed with status code: {0}'.format(res.status_code))
            print(res.text)
            exit(1)
        return

    def cancel_domain(self, domain, immediately=False):
        if immediately:
            data = '{"endTime": "immediately"}'
        else:
            data = '{"endTime": "end"}'
        url = self.base_url + '/' + domain
        res = requests.delete(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Canceling domain failed with status code: {0}'.format(res.status_code))
            print(res.text)
            exit(1)
        return

    def get_domain_branding(self, domain):
        url = self.base_url + '/' + domain + '/branding'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Get domain branding for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def update_domain_branding(self, domain, data):
        url = self.base_url + '/' + domain + '/branding'
        res = requests.put(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Update domain branding for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return

    def list_contacts(self, domain):
        url = self.base_url + '/' + domain + '/contacts'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('List domain contacts for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def update_contacts(self, domain, data):
        url = self.base_url + '/' + domain + '/contacts'
        res = requests.put(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Update contacts for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return

    def list_dns_entries(self, domain):
        url=self.base_url + '/' + domain + '/dns'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Getting dns entries for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def add_dns_entry(self, domain, data):
        url = self.base_url + '/' + domain + '/dns'
        res = requests.post(url, headers=self.headers, data=data)
        if res.status_code != 201:
            print('Creating dns entry for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            print('Data was: {0}'.format(data))
            exit(1)
        return

    def update_dns_entry(self, domain, data):
        url = self.base_url + '/' + domain + '/dns'
        res = requests.patch(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Updating dns entry for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return

    def update_all_dns_entries(self, domain, data):
        url = self.base_url + '/' + domain + '/dns'
        res = requests.put(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Updating all dns entries for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return

    def delete_dns_entry(self, domain, data):
        url = self.base_url + '/' + domain + '/dns'
        res = requests.delete(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Deleting dns entry for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return