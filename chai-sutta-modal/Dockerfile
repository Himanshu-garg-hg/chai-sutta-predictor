FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r chai-sutta-modal/requirements.txt
EXPOSE 5000
CMD ["python", "chai-sutta-modal/src/app.py"]