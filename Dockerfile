FROM python:3.8-slim

WORKDIR /app
COPY . .
RUN pip install -r ./requirements.txt
CMD gunicorn resume.wsgi:application --bind 0:8000