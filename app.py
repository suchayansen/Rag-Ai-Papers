from src.ingestion import load_data
from src.pipeline import run_pipeline
from src.generator import generate_answer

DATA_PATH = "data/ai_papers.csv"

def main():
    df = load_data(DATA_PATH)
    query = input("Ask a research question: ")
    contexts = run_pipeline(query, df)
    answer = generate_answer(query, contexts)
    print(answer)

if __name__ == "__main__":
    main()
