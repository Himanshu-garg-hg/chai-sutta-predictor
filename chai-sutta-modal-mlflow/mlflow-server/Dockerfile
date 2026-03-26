FROM python:3.10-slim

WORKDIR /app

RUN pip install mlflow azure-storage-blob
RUN mkdir -p /mlflow/artifacts && chmod -R 777 /mlflow

EXPOSE 5000

CMD mlflow server \
    --host 0.0.0.0 \
    --port 5000 \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root /mlflow/artifacts \
    --allowed-hosts "*"