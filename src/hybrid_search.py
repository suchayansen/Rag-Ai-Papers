def hybrid_search(bm25_results, vector_results, alpha=0.5):
    scores = {}

    for rank, idx in enumerate(bm25_results):
        scores[idx] = scores.get(idx, 0) + alpha / (rank + 1)

    for rank, idx in enumerate(vector_results):
        scores[idx] = scores.get(idx, 0) + (1 - alpha) / (rank + 1)

    return sorted(scores, key=scores.get, reverse=True)
