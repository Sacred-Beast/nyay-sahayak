import chromadb
from sentence_transformers import SentenceTransformer
from .config import CHROMA_HOST, CHROMA_PORT, EMBEDDING_MODEL

def get_chroma_client():
    return chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)

def embed_query(query):
    model = SentenceTransformer(EMBEDDING_MODEL)
    return model.encode([query])[0].tolist()

def semantic_search(case_id, query, top_k=5):
    client = get_chroma_client()
    collection = client.get_or_create_collection(name="legal_cases")
    embedding = embed_query(query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
        where={"case_id": case_id}
    )
    return [doc for doc in results["documents"][0]]
