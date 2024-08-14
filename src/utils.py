from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

def get_groq_api_key():
    return os.getenv("GROQ_API")
    
def connect_to_groq():
    return Groq(api_key=get_groq_api_key())