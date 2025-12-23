
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Trade Opportunities API"
    VERSION: str = "1.0.0"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    API_KEY: str = os.getenv("API_KEY", "secret-token")  # simple auth for the API itself

settings = Settings()
