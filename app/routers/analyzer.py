from fastapi import APIRouter, UploadFile, File
from typing import List
from app.services.jd_loader import load_job_description
from app.services.evaluator import evaluate_uploaded_resumes
from app.models.match_result import BatchMatchResponse

router = APIRouter()

@router.post("/evaluate", response_model=BatchMatchResponse)
async def evaluate_resumes(resumes: List[UploadFile] = File(..., media_type="application/pdf")) -> BatchMatchResponse:
    """
    Accepts multiple resume PDFs and evaluates them against the stored JD.
    """
    jd_text: str = load_job_description()
    results = evaluate_uploaded_resumes(resumes, jd_text)
    return BatchMatchResponse(
        job_description="jd.pdf",
        results=results
    )
