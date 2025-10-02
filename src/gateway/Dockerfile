FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y \
--no-install-recommends --no-install-suggests \
build-essential \
pkg-config \
libssl-dev

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

CMD ["python", "server.py"]