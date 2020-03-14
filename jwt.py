#!/usr/bin/env python3

from OpenSSL import crypto
import base64
key_file = open("test.pem", "r")
key = key_file.read()
key_file.close()
print(key)
print()
if key.startswith('-----BEGIN '):
    pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
else:
    pkey = crypto.load_pkcs12(key).get_privatekey()
print (pkey)
print()
data = b'''{ "login": "usernam", "nonce": "98475920834" }'''
sign = crypto.sign(pkey, data, "sha512") 
print (sign)
print()
data_base64 = base64.b64encode(sign)
print (data_base64.decode())

# curl -H 'Signature: B6Zend6DCaUgkTBuuvYDx3C3VqzBAyHFNtq567+72BaIR+0I7Bau+6DJrbkbgEWguZgVmrjGGnF2w8nviAQbkMxHd4A5gjarradJlU/b2rvzZuvQd1LgnGECop2n6yJg7u9uTgxaUZ4yK0f60NYbogUVGfjit9rT7E+I2PmC2z2UlSVW/6l9S19zdHvTEi1k8TTSSeF8g5yW5cml6QaBqWACzGoJk3N4ktwG7Q8wM/mX5etv6Ytbr0JJLvDe6BruBONrfWPdvtj8ikGhZpJUY4vN1Pwm0Vd4E+oy18Ul1kCqN323aBOEw05ZGtFkZuohCj2E6/SsNyk8LO4DAsPCTQ==' -H "Accept: application/json" -d '{ "login": "jvgemert", "nonce": "98475920834" }' https://api.transip.nl/v6/auth -X POST 

