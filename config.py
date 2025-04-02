import os
from dotenv import load_dotenv

load_dotenv()

Gemini_API_KEY = os.getenv("GEMINI_API_KEY")
Openai_API_KEY = os.getenv("OPENAI_API_KEY")