def generate_answer(query, contexts):
    combined_context = " ".join(contexts)
    return f"""
Question:
{query}

Answer (based on retrieved research papers):
{combined_context[:700]}...
"""
