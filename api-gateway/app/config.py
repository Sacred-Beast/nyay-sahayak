import os
from dotenv import load_dotenv

load_dotenv()

INGESTION_URL = os.getenv("INGESTION_URL", "http://ingestion:8001")
RAG_URL = os.getenv("RAG_URL", "http://rag:8002")
FACT_CHECKER_URL = os.getenv("FACT_CHECKER_URL", "http://fact_checker:8003")
SHARED_DATA_PATH = os.getenv("SHARED_DATA_PATH", "/shared_data")
