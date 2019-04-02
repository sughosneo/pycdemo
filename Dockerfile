FROM ubuntu:18.04

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip


RUN apt-get install -y vim

RUN mkdir -p /pycdemo
WORKDIR /pycdemo
COPY ./ /pycdemo/

RUN pip3 install -r requirements.txt