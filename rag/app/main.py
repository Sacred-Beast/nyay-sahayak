from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .chroma_utils import semantic_search
from .gemini_client import call_gemini
from .prompt_engineering import build_prompt

app = FastAPI(
    title="Nyay-Sahayak RAG Service",
    description="Retrieval-Augmented Generation for legal argumentation.",
    version="1.0.0"
)

class AnalyzeRequest(BaseModel):
    case_id: str
    user_query: str

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    # Retrieve relevant context
    context = semantic_search(req.case_id, req.user_query)
    # For demo, just concatenate all chunks as case_text
    case_text = " ".join(context)
    # Claims: for demo, use first 3 sentences as claims
    claims = context[:3]
    prompt = build_prompt(context, case_text, claims, req.user_query)
    try:
        output = call_gemini(prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"argument": output}
