FROM python-3.11-slim

WORKDIR /app
ADD index.html /app
ADD main.py /app

ENTRYPOINT /app/main.py
