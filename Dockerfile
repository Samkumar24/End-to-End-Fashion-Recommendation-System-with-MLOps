FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN mkdir -p artifacts/feature_engineering/model
RUN mkdir -p artifacts/feature_engineering/featured_data

RUN python docker_run_pipline.py

EXPOSE 8000
EXPOSE 8501

CMD ["sh", "-c", "echo 'Streamlit : http://localhost:8501' && echo 'FastAPI : http://localhost:8000/docs' && uvicorn fast_api:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port 8501 --server.address 0.0.0.0"]