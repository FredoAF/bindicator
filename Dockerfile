FROM python:alpine
RUN pip install requests
COPY bindicator.py /bindicator.py
ENTRYPOINT ["/usr/local/bin/python", "/bindicator.py"]