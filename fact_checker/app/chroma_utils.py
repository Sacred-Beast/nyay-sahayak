import chromadb
from sentence_transformers import SentenceTransformer
from .config import CHROMA_HOST, CHROMA_PORT, EMBEDDING_MODEL

def get_chroma_client():
    return chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)

def embed_sentences(sentences):
    model = SentenceTransformer(EMBEDDING_MODEL)
    return model.encode(sentences).tolist()

def get_case_chunks(case_id):
    client = get_chroma_client()
    collection = client.get_or_create_collection(name="legal_cases")
    results = collection.get(where={"case_id": case_id})
    return results["documents"], results["embeddings"]
