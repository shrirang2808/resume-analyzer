from PyPDF2 import PdfReader
from app.config import JD_PATH

def load_job_description() -> str:
    """
    Loads and extracts text from the static job description PDF.
    """
    reader = PdfReader(JD_PATH)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
