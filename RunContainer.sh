#!/bin/sh

docker-compose down -v 
docker-compose up -d --build
docker exec openai-api-docker_openai-api-docker_1 streamlit run openai-api-docker/test.py
