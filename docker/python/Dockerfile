FROM python:3.8-alpine

COPY ./docker/python/requirements.txt /tmp/requirements.txt

WORKDIR /application

RUN apk update \
    && apk add gcc \
        musl-dev \
        cyrus-sasl-dev \
        zlib-dev \
        make \
        git \
        libffi \
        libffi-dev \
        openssl-dev \
    && pip install --no-cache-dir -r /tmp/requirements.txt

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"