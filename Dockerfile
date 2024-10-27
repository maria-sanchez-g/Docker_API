# Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

COPY . .

# No CMD here since each service specifies its own command in docker-compose.yml
