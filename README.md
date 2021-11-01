# transip_ddns

This can be used as a script to update your dns entry at Transip to your public ip like a dynamic dns.

./transip_ddns.py -l [TRANSIP_USERNAME] -f [FILE_THAT_CONTAINS_TRANSIP_API_KEY] -d [DOMAIN_NAME] -e [DOMAIN_ENTRY]

example:

```./transip_ddns.py -l jeromba6 -f ddns.pem -d example.com -e www```

This would retreive you public IP and make sure www.example.com contains an A-record that contains this public IP.

There is also a docker image avalible you can use it in the following way:

docker run -it -v [DIR_THAT_CONTAINS_FILE_THAT_CONTAINS_TRANSIP_API_KEY]:/keydir ghcr.io/jeromba6/transip_ddns/transip_ddns:1.1 -l [TRANSIP_USERNAME] -d [DOMAIN_NAME] -e [DOMAIN_ENTRY] -f /keydir/[FILE_THAT_CONTAINS_TRANSIP_API_KEY]

example:

```docker run -it -v /home/jeromba6/keydir:/keydir ghcr.io/jeromba6/transip_ddns/transip_ddns:1.1 -l jeromba6 -d example.com -e www -f /keydir/transip-ddns.pem```
