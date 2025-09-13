from openai import AzureOpenAI
from app.utils.env_loader import AZURE_API_KEY, AZURE_ENDPOINT, AZURE_API_VERSION, CHAT_MODEL

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION,
    azure_endpoint=AZURE_ENDPOINT
)

def generate_match_summary(jd_text: str, resume_text: str) -> str:
    """
    Uses GPT-4 to evaluate resume against JD and generate a match summary.
    """
    prompt = f"""
    You are a resume evaluator. First, verify if the following text is a valid resume. If not, say so and skip evaluation.

    Resume:\n{resume_text}

    If valid, compare it to the JD below and provide match score, strengths, and gaps.

    JD:\n{jd_text}
    """

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content
