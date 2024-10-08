from dotenv import load_dotenv
from groq import Groq
from serpapi import GoogleSearch
import os
import re
from typing import List

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

    get_gdp:
    e.g. get_gdp: India 2023
    This action runs a google search and returns the gdp of a country in USD in the provided year.

    Example Session
    Question: What is the ratio between the GDP of India and Chain in 2023?
    Thought: I need to get the GDP of India in the year 2023
    Action: get_gdp: India 2023
    PAUSE
    After deciding on an Action you will PAUSE and wait to be provided with an Observation and recalled.

    You will be called again with an Observation:
    Observation: The statistic shows GDP in India from 1987 to 2023, with projections up until 2029. In 2023, GDP in India was at around 3.57 trillion U.S. dollars, and it is expected to reach six trillion by the end of the decade


    Thought: I need to get the GDP of Chain in the year 2023
    Action: get_gdp: China 2023
    PAUSE
    After deciding on an Action you will PAUSE and wait to be provided with an Observation and recalled.

    You will be called again with an Observation:
    Observation: Gross domestic product (GDP) of China 1985-2029. In 2023, the gross domestic product (GDP) of China amounted to around 17.7 trillion U.S. dollars.


    Thought: I need to find the ratio between the GDP of both the countries
    Action: calculate: 1 / (3.737 / 17.7) 
    PAUSE
    After deciding on an Action you will PAUSE and wait to be provided with an Observation and recalled.

    You will be called again with an Observation:
    Observation: 1:4.78

    If you have the answer, Output it as the answer
    Answer: The ratio of the GDP of India and China in the year 2023 is 1:4.78

    Now it's your turn:
    """.strip()

    return prompt

def calculate(question):
    print("CALCULATE FUNCTION CALLED")
    return eval(question)

def get_serp_api_key():
    return os.getenv('SERPAPI_API_KEY')

def get_gdp(input_list: List[str]):
    print("GET GDP FUNCTION CALLED")
    search = GoogleSearch({
        'q': f'What is/was the GDP of {input_list[0]} in the year {input_list[1]} in USD',
        'api_key':get_serp_api_key()
    })
    return search.get_dict()

def get_function_name_and_parameters(action):
    #return re.search(r"Action:\s*(\w+):\s*(.*)", action)
    pattern = r"Action:\s*(\w+):\s*(.+)"
    return re.search(pattern, action)

if __name__=='__main__':
    Action = """
    Thought: I need to find the ratio between the GDP of India and USA in the year 2023
    Action: calculate: China 2023
    """
    output = get_function_name_and_parameters(Action)
    print(output)
    print(output.group(1))
    print(output.group(2).split())
    tools_map = {'calculate':calculate}
    result = tools_map[output.group(1)](output.group(2))
    print(result)