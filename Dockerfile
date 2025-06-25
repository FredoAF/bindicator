FROM python:alpine

COPY bindication.py /bindicator.py
ENTRYPOINT ["/usr/local/bin/python", "/bindicator.py"]