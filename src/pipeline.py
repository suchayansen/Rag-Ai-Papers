from src.preprocessing import clean_text
from src.embeddings import generate_embeddings
from src.vector_store import VectorStore
from src.bm25_search import BM25Search
from src.hybrid_search import hybrid_search
from src.logger import logger

def run_pipeline(query, df, top_k=3):
    logger.info("Starting RAG pipeline")

    corpus = [clean_text(text) for text in df["abstract"]]

    # BM25 Search
    bm25 = BM25Search(corpus)
    bm25_results = bm25.search(query)

    # Vector Search
    embeddings = generate_embeddings(corpus)
    store = VectorStore(embeddings.shape[1])
    store.add_embeddings(embeddings)

    query_embedding = generate_embeddings([query])[0]
    vector_results = store.search(query_embedding)

    # Hybrid Ranking
    final_indices = hybrid_search(bm25_results, vector_results)

    return [df.iloc[i]["abstract"] for i in final_indices[:top_k]]
