from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from .config import SHARED_DATA_PATH
from .utils import extract_text_from_pdf
from .argument_mining import mine_arguments
from .chroma_utils import embed_chunks, store_chunks_in_chroma
from .neo4j_utils import populate_graph, get_case_subgraph

app = FastAPI(
    title="Nyay-Sahayak Ingestion Service",
    description="Ingests legal documents, mines arguments, and populates databases.",
    version="1.0.0"
)

class IngestRequest(BaseModel):
    filename: str

@app.post("/ingest")
def ingest(req: IngestRequest):
    pdf_path = os.path.join(SHARED_DATA_PATH, req.filename)
    if not os.path.exists(pdf_path):
        raise HTTPException(status_code=404, detail="File not found")
    text = extract_text_from_pdf(pdf_path)
    entities, claims, premises = mine_arguments(text)
    # Chunking
    chunk_size = 512
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    embeddings = embed_chunks(chunks)
    case_id = req.filename.replace(".pdf", "")
    store_chunks_in_chroma(case_id, chunks, embeddings)
    populate_graph(case_id, entities, claims, premises)
    return {"case_id": case_id, "entities": entities, "claims": claims, "premises": premises}

@app.get("/graph/{case_id}")
def graph(case_id: str):
    return get_case_subgraph(case_id)
