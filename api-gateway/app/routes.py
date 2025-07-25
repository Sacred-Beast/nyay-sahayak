# routes main file

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import httpx
import os
from .config import INGESTION_URL, RAG_URL, FACT_CHECKER_URL, SHARED_DATA_PATH
from .utils import save_upload_file

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    filename = file.filename
    dest_path = os.path.join(SHARED_DATA_PATH, filename)
    save_upload_file(file, dest_path)
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{INGESTION_URL}/ingest", json={"filename": filename})
        if resp.status_code != 200:
            raise HTTPException(status_code=500, detail="Ingestion failed")
        return resp.json()

@router.post("/analyze")
async def analyze_case(case_id: str = Form(...), user_query: str = Form(...)):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{RAG_URL}/analyze", json={"case_id": case_id, "user_query": user_query})
        if resp.status_code != 200:
            raise HTTPException(status_code=500, detail="RAG failed")
        return resp.json()

@router.post("/fact-check")
async def fact_check(case_id: str = Form(...), argument: str = Form(...)):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{FACT_CHECKER_URL}/fact-check", json={"case_id": case_id, "argument": argument})
        if resp.status_code != 200:
            raise HTTPException(status_code=500, detail="Fact-check failed")
        return resp.json()

@router.get("/graph/{case_id}")
async def get_graph(case_id: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{INGESTION_URL}/graph/{case_id}")
        if resp.status_code != 200:
            raise HTTPException(status_code=500, detail="Graph fetch failed")
        return resp.json()
