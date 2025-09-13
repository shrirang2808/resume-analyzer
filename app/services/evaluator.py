from fastapi import UploadFile
from app.services.embedding_engine import embed_text
from app.services.llm_engine import generate_match_summary
from app.models.match_result import ResumeMatch
from app.services.jd_loader import load_job_description
from PyPDF2 import PdfReader
from docx import Document
from sklearn.metrics.pairwise import cosine_similarity
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(file: UploadFile) -> str:
    """
    Extracts text from PDF or DOCX file.
    """
    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    
    elif file.filename.endswith(".docx"):
        doc = Document(file.file)
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    
    else:
        return ""

def extract_candidate_name(text: str) -> str:
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Unknown"

def is_valid_resume(text: str) -> bool:
    """
    Checks if the uploaded text contains enough resume-like keywords.
    Returns True if it's likely a resume, False otherwise.
    """
    keywords = ["experience", "skills", "education"]
    return sum(kw in text.lower() for kw in keywords) >= 3

def evaluate_uploaded_resumes(files: list[UploadFile], jd_text: str) -> list[ResumeMatch]:
    jd_embedding = embed_text(jd_text)
    results = []
    
    for file in files:
        if not file.filename.endswith((".pdf", ".docx")):
            results.append(ResumeMatch(
                resume_filename=file.filename,
                candidate_name="Unknown",
                match_score=0.0,
                strengths=[],
                gaps=[],
                summary="Unsupported file type. Only PDF and DOCX resumes are accepted."
            ))
            continue

        resume_text = extract_text(file)

        if not is_valid_resume(resume_text):
            results.append(ResumeMatch(
            resume_filename=file.filename,
            candidate_name="Unknown",
            match_score=0.0,
            strengths=[],
            gaps=[],
            summary="This file does not appear to be a resume. Skipping evaluation."
            ))
            continue
        
        resume_embedding = embed_text(resume_text)
        similarity = float(cosine_similarity([resume_embedding], [jd_embedding])[0][0])
        summary = generate_match_summary(jd_text, resume_text)
        candidate_name = extract_candidate_name(resume_text)

        results.append(ResumeMatch(
            resume_filename=file.filename,
            candidate_name=candidate_name,
            match_score=round(similarity, 2),
            strengths=[],  # Optional: parse from summary
            gaps=[],       # Optional: parse from summary
            summary=summary
        ))

    return results
