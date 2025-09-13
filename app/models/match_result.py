from pydantic import BaseModel
from typing import List

class ResumeMatch(BaseModel):
    resume_filename: str
    candidate_name: str
    match_score: float
    strengths: List[str]
    gaps: List[str]
    summary: str

class BatchMatchResponse(BaseModel):
    job_description: str
    results: List[ResumeMatch]
