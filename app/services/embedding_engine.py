from openai import AzureOpenAI
from app.utils.env_loader import AZURE_API_KEY, AZURE_ENDPOINT, AZURE_API_VERSION, EMBED_MODEL
from typing import List

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    api_version=AZURE_API_VERSION,
    azure_endpoint=AZURE_ENDPOINT
)

def embed_text(text: str) -> List[float]:
    """
    Generates embedding for a given text using Azure OpenAI.
    """
    response = client.embeddings.create(
        input=[text],
        model=EMBED_MODEL
    )
    return response.data[0].embedding
