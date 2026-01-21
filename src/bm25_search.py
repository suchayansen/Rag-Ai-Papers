from rank_bm25 import BM25Okapi

class BM25Search:
    def __init__(self, corpus):
        tokenized = [doc.split() for doc in corpus]
        self.bm25 = BM25Okapi(tokenized)

    def search(self, query, k=5):
        scores = self.bm25.get_scores(query.split())
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return ranked[:k]
