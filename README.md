# transip_ddns

This can be used as a script to update your dns entry at Transip to your public ip like a dynamic dns.

./transip_ddns.py -l [TRANSIP_USERNAME] -f [FILE_THAT_CONTAINS_TRANSIP_API_KEY] -d [DOMAIN_NAME] -e [DOMAIN_ENTRY]

example:

./transip_ddns.py -l jeromba6 -f ddns.pem -d example.com -e www
