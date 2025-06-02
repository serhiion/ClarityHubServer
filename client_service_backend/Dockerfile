FROM python:3.11-slim

WORKDIR /app

COPY client_service_backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY client_service_backend /app/client_service_backend

EXPOSE 8000

CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "client_service_backend.run:app"]
