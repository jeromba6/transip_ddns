#!/usr/bin/env python3

"""setdns.py retrives the public IP and sets it to a predefinde DNS entry"""

__author__      = "Jeroen van Gemert"
__copyright__   = "Copyright 2020, Planet Earth"

import urllib.request
import json
from transip.service.domain import DomainService

# contents = json.loads(urllib.request.urlopen("http://ipinfo.io").read())
# print (json.dumps(contents,indent=2))
basedomain='gemert.net'
domainentry='update-test'
key='''-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDIYjaYtIh8EDSu
wmVxRaXm6gtA9cRGds2juYvO+za8oQ+36OS4J35Hig/XE0Zr1hrfjGfnuy3bubrj
zB/w3Hg4Kl63oBel/2HSmaNczR12dMGZzMqyHHXyZKl/cYjzhbgAucSM/q+inbuL
1gK0O9+Ov2Uc8iMfeRBG/XBNo5QVVzWYF+BSmojobawGMIR/LKKKJL6HNzdcz5yr
PAWR0HfukpwuZcehEJca/TLgUf/FoBfRKm+tFVyVNYB6v2kvI0ASMMhsnsEnQ0CX
0mi9cmyXB6iB/5SnwKkXZIwPXwmyXvSwIdZiTU70QNlfGKrIGuv5+fDNd1+g7XDV
yjzS9HObAgMBAAECggEAIDSQu8hAK1hbbz71GNhtyogRGPam/gA4GrlGfBSp/nUQ
VqmKoQJP7GWHGDUT218E4KrrRDY0L51RKS10cLyuYbCFmpOTWW2LJlLlC5Q3yQMI
3pQoe6nRVwzQpRf1P9Zc9Vjl+xcv2T3ql5Xkx1zcGFAwiw9rj7JgaFhxRTkmIquh
oyHkMHW74hSVlx55HhDtc1uTK3aWnEhKJfj/dRmA5Hald3ixoaASsZWA3ZTr7B8R
b/2mAGml+/dEYuspbkIZW9Bryv7UlpT2E9/7SpV8c05Spehl12EfMcJhaFJDe1G4
kkCqbl8Uks+jm9/aWSUIUzcHuZDw1PAiVqPVVcyfkQKBgQDtHp89U1QZBuAXI3KM
FOeOFUD+Vb4oLhTyWVsWE6jJjxfGVyGtIRNw6rHrHumlN8Fpb4ijEdvoNQkPiKnl
HYGnUp7BkbvpgncjL6b4br3b9cXtcpDHdTD5dAir+j3sDrVvAG6YXnuyZONOXxXm
oVp/sd+DBArBQFqHgQICOxgNowKBgQDYVsaZEoa22tuhrVfo5UxoRq+hAnMN5cTv
iGof1Qt2t2BYVEjpz2YpVQ/ksCHbtSVxRzw00qW4xzHNzxJ4JkDAlerxQy+nqBCp
emWMADs2H/ALTvCFaEA+rGLe+MYf0ANaw94AbR44jKNcGqMrwwVQpC9CY3/C0A9L
pg1ssZ/xqQKBgFZrG6QRE4xPeipUq/GryLx6uIY5H6WrLc0pjc3c+l4DPan2pXpg
nKJBlvhW+tZRHLddg9HSt2/IrHWx3CF5gIBH1z46695twxfazSKr0Zwx1aH1aBiZ
eHDhvitXd2vp7Gv5H1V+0dwxcrpkYyn70mzJmek49uZ5msTZ2q6PdPO7AoGAapi3
Wo1KW6cTOWLUQilZsLfDqi4uytZAZ1ZsFCtBbsmEa4F8O9i5mfwTzLcMt9lWDa7v
94cjqRxdae9yRkly9nHoReC5Bn9FVny8tHMYud6axLesw89OeJMwVHV4CgzQ2lRQ
ex1JGswRYjyt0c5SPB3qO2gTd8ZVAw1a6AfNq6ECgYB/tndONcYppD/j3278+3Wy
EV/P0CEBVrvXboUyxkFykZ5CFYkpNEisQ4Imu9PUGCOqSxxOoXQ2TyyzIb9nY1g1
K2Xs9J9sOEoGmmWJ+RJkHiwNkAIAbuYaluqtRyqY0w2z19JZKRv1u9vuWP1+f5G6
+5aF0x9Xgt2Tvq3T1caywg==
-----END PRIVATE KEY-----'''

dnsservice = DomainService('jvgemert', private_key=key)
#print(dnsservice.get_domain_names())
# print(dnsservice.batch_get_info(['gemert.net','just4ward.net']))
#print(dnsservice.check_availability(basedomain))
entries=dnsservice.get_info(basedomain)
print(entries)




# print(dnsservice.check_availability('jeroenbladibla.nl'))
