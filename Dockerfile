FROM python:alpine

COPY bindicator.py /bindicator.py
ENTRYPOINT ["/usr/local/bin/python", "/bindicator.py"]