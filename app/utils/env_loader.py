from dotenv import load_dotenv
import os

load_dotenv()

AZURE_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
EMBED_MODEL = os.getenv("AZURE_OPENAI_EMBED_MODEL")
CHAT_MODEL = os.getenv("AZURE_OPENAI_CHAT_MODEL")
