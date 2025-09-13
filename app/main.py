from fastapi import FastAPI
from app.routers import analyzer

app = FastAPI(title="Resume Analyzer API")
app.include_router(analyzer.router, prefix="/analyzer", tags=["Resume Matching"])
