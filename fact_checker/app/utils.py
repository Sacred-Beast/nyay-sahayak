import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize
from numpy import dot
from numpy.linalg import norm

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b) + 1e-8)

def split_sentences(text):
    return sent_tokenize(text)
