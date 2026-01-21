# Project Overview
This project implements a production-ready Retrieval-Augmented Generation (RAG) pipeline over a dataset of AI research papers.
The system retrieves relevant research content using a hybrid search approach (BM25 + vector similarity) and generates answers grounded in retrieved documents.
The project is designed with clean architecture, modular code structure, logging, and robust data handling, as required for the interview assignment.
## 🗂️ Project Structure
rag-ai-papers/
app.py                 
├── requirements.txt      
├── README.md               
├── data/

│   ── ai_papers.csv      

├── src/

│   ├── init.py   
|     ├── logger.py           
│   ├── ingestion.py        
│   ├── preprocessing.py   
│   ├── embeddings.py       
│   ├── vector_store.py   
│   ├── bm25_search.py     
│   ├── hybrid_search.py   
│   ├── generator.py      
│   └── pipeline.py        
│
└── .gitignore

## 🧠 Architecture Overview
User Query → Hybrid Retrieval (BM25 + FAISS) → Relevant Documents → Response Generation → Final Answer
## ⚙️ Setup Instructions
### 1️⃣ Clone the Repository
git clone <your-github-repo-url>

cd rag-ai-papers
### 2️⃣ Create Virtual Environment
python -m venv venv
#### Activate it:
venv\Scripts\activate
### 3️⃣ Install Dependencies
pip install --upgrade pip

pip install -r requirements.txt
### 4️⃣ Add Dataset
data/ai_papers.csv
### ▶️ Usage Instructions
python app.py


