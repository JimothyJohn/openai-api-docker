FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
	python3 python3-pip

WORKDIR /

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

ENV OPENAI_API_KEY=$OPENAI_API_KEY