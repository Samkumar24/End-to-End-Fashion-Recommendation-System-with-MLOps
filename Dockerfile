FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000
EXPOSE 8501
EXPOSE 5001

CMD ["sh", "-c", "mlflow server --backend-store-uri sqlite:///mlflow.db --host 0.0.0.0 --port 5001 & uvicorn fast_api:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port 8501 --server.address 0.0.0.0"]