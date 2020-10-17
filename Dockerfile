FROM python:3.9.0
COPY transip_ddns.py /

RUN pip install transipApiV6 requests crypto pyOpenSSL
ENTRYPOINT [ "python", "/transip_ddns.py" ]