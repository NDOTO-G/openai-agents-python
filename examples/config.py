from agents import set_default_openai_key
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key for the SDK
set_default_openai_key(os.getenv("OPENAI_API_KEY")) 