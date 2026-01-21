from sentence_transformers import SentenceTransformer
from src.logger import logger

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(texts):
    logger.info("Generating embeddings...")
    return model.encode(texts, show_progress_bar=True)
