from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .chroma_utils import embed_sentences, get_case_chunks
from .utils import split_sentences, cosine_similarity

app = FastAPI(
    title="Nyay-Sahayak Fact Checker",
    description="Fact-checks generated legal arguments.",
    version="1.0.0"
)

class FactCheckRequest(BaseModel):
    case_id: str
    argument: str

@app.post("/fact-check")
def fact_check(req: FactCheckRequest):
    sentences = split_sentences(req.argument)
    arg_embeddings = embed_sentences(sentences)
    case_chunks, chunk_embeddings = get_case_chunks(req.case_id)
    results = []
    for sent, emb in zip(sentences, arg_embeddings):
        sims = [cosine_similarity(emb, chunk_emb) for chunk_emb in chunk_embeddings]
        max_idx = int(max(range(len(sims)), key=lambda i: sims[i]))
        max_sim = sims[max_idx]
        status = "Verified" if max_sim > 0.75 else "Needs Review"
        results.append({
            "sentence": sent,
            "status": status,
            "supporting_text": case_chunks[max_idx],
            "similarity": round(float(max_sim), 3)
        })
    return {"fact_check": results}
