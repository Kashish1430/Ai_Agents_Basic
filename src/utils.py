from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

def get_groq_api_key():
    return os.getenv("GROQ_API")
    
def connect_to_groq():
    return Groq(api_key=get_groq_api_key())

def get_prompt():
    prompt = """
    You run in a loop of THOUGHT, ACTION, PAUSE and OBSERVATION.
    At the end of the loop you return an ANSWER.
    Use Thought to showcase your thought process of the given query.
    Use Action to chose one of the available and most suitable action and then return PAUSE.
    OBSERVATION will be the result of you using those actions.

    Your available actions are:
    calculate:
    e.g. calculate: 12^2 * 7^3
    This action runs a calculation and returns a number as a result - This action uses python, so be sure to use floating point syntax wherever necessary


    """

def calculate(question):
    return eval(question)