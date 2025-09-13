#  Resume Analyzer – GenAI + RAG Powered Backend

This project is a backend API built with **FastAPI** and **Azure OpenAI**, designed to evaluate multiple resumes against a stored job description (JD) using **LLM-based reasoning** and **retrieval-augmented generation (RAG)**.

---

##  Use Case

HR teams or recruiters can upload multiple resumes in one request. The backend:
- Loads a static JD stored in the backend
- Extracts and validates resume content (PDF or DOCX)
- Uses Azure OpenAI embeddings for semantic similarity
- Prompts GPT-4 to generate match summaries
- Returns structured results with match score, strengths, gaps, and candidate name

---

##  Tech Stack

- **FastAPI** – High-performance Python API framework
- **Azure OpenAI** – GPT-4 and text-embedding-ada-002
- **RAG** – Retrieval-Augmented Generation for grounded evaluation
- **spaCy** – Named Entity Recognition for candidate name extraction
- **PyPDF2 / python-docx** – Resume text extraction
- **scikit-learn** – Cosine similarity scoring

---

## 🧰 Prerequisites

- Python 3.10+
- Azure OpenAI resource with:
  - GPT-4 deployment
  - Embedding model deployment
- API keys and endpoint stored in `.env`

---

## ⚙️ Setup Instructions

### 1. Clone the repo

### 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

### 4. Create .env file
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-07-01-preview
AZURE_OPENAI_EMBED_MODEL=your-embedding-deployment-name
AZURE_OPENAI_CHAT_MODEL=your-gpt-deployment-name

### 5. Add your JD file
Place your jd.pdf inside: data/job_description/jd.pdf

### 6. Run the API
uvicorn app.main:app --reload
Visit the swagger UI at: http://localhost:8000/docs
Use the /analyzer/evaluate endpoint to upload multiple resumes and test.

### 7. Features
Batch resume evaluation

PDF and DOCX support

Resume validation and filtering

LLM-generated match summaries

Named entity extraction for candidate names

Structured API response for easy frontend integration

### 8. Folder Structure
resume-analyzer/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routers/
│   ├── services/
│   ├── models/
│   └── utils/
├── data/
│   ├── resumes/
│   └── job_description/
├── requirements.txt
├── .env
├── .gitignore
