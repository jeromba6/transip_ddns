FROM python:3.9.7-slim
COPY transip_ddns.py /

RUN pip install transipApiV6 requests crypto pyOpenSSL
ENTRYPOINT [ "python", "/transip_ddns.py" ]