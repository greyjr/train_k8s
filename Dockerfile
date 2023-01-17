
FROM python:3.10.0-slim

ARG version
ENV BOT_VERSION=${version}
ENV PYTHONPATH=/app

COPY requirements/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY app /app
EXPOSE 8080

CMD ["python", "main.py"]
