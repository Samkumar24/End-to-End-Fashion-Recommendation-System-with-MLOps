FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN  pip install -r requirements.txt

EXPOSE 8000
EXPOSE 8501
EXPOSE 50001

CMD ["sh", "-c", "mlflow server --host 0.0.0.0 --port 5001 & uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port 8501 --server.address 0.0.0.0"]