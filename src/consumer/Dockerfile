FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y \
--no-install-recommends --no-install-suggests \
build-essential \
ffmpeg \ 
&& pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "consumer.py"]