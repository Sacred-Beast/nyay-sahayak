import chromadb
from sentence_transformers import SentenceTransformer
from .config import CHROMA_HOST, CHROMA_PORT, EMBEDDING_MODEL

def get_chroma_client():
    return chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)

def embed_chunks(chunks):
    model = SentenceTransformer(EMBEDDING_MODEL)
    return model.encode(chunks).tolist()

def store_chunks_in_chroma(case_id, chunks, embeddings):
    client = get_chroma_client()
    collection = client.get_or_create_collection(name="legal_cases")
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            metadatas=[{"case_id": case_id, "chunk_id": i}]
        )
