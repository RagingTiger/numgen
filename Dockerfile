FROM python:3.9.0a3-alpine3.10

# get numgen source
COPY numgen.py /usr/src

WORKDIR /home/numgen
