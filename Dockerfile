FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

VOLUME ./credentials/credentials.json:/app/credentials/credentials.json

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials/credentials.json

COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]