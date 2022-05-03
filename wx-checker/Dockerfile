FROM python:3.10

WORKDIR /wx-checker

COPY . .

RUN apt-get update

RUN pip install --no-cache-dir -r requirements.txt

ENV TZ Europe/Moscow

EXPOSE 8765

ENTRYPOINT python3 weather_checker.py

