import os
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai_key = os.getenv("OPENAI_API_KEY")

def set_response(mensagens, openai_key, modelo="gpt-4o-mini",temperature=0.5, strem=False):
    openai.api_key = openai_key
    response = openai.Completion.create(
        model=modelo,
        messages=mensagens,
        temperature=temperature,
        strem=strem
    )
    return response