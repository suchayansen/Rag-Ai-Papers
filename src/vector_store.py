import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings):
        self.index.add(np.array(embeddings))

    def search(self, query_embedding, k=5):
        _, indices = self.index.search(
            np.array([query_embedding]), k
        )
        return indices[0]
