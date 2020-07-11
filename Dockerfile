FROM python:3.8-slim as base

RUN apt-get update && \
    apt-get install --yes build-essential autoconf libtool pkg-config \
    libgflags-dev libgtest-dev clang libc++-dev automake libpq-dev git curl

RUN mkdir /var/app/

RUN python3.8 -m pip install --upgrade pip

COPY ./requirements.txt /var/app

RUN cd /var/app && python3.8 -m pip install -r requirements.txt

COPY . /var/app

WORKDIR /var/app

EXPOSE 8000

RUN chmod +x start.sh

ENTRYPOINT ["./start.sh"]
