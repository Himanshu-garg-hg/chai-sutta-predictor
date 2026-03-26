FROM python:3.10-slim

WORKDIR /app

RUN pip install mlflow azure-storage-blob
# RUN mkdir -p /mlflow/artifacts && chmod -R 777 /mlflow

EXPOSE 5000

# CMD mlflow server \
#     --host 0.0.0.0 \
#     --port 5000 \
#     --backend-store-uri sqlite:///mlflow.db \
#     --default-artifact-root /mlflow/artifacts \
#     --allowed-hosts "*"


CMD mlflow server \
    --host 0.0.0.0 \
    --port 5000 \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root "wasbs://chai-sutta-container@modalstorageacc.blob.core.windows.net/mlflow?sp=racwdli&st=2026-03-26T12:36:11Z&se=2026-03-26T16:51:11Z&sv=2024-11-04&sr=c&sig=UTgFJNPWMrhplXLr08usJtdaekZCRJy3IXqX949kxBU%3D" \
    --allowed-hosts "*"