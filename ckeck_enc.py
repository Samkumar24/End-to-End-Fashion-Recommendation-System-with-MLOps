from dotenv import load_dotenv
import os

load_dotenv()

print("URI      :", os.getenv("MLFLOW_TRACKING_URI"))
print("USERNAME :", os.getenv("MLFLOW_TRACKING_USERNAME"))
print("PASSWORD :", os.getenv("MLFLOW_TRACKING_PASSWORD"))
