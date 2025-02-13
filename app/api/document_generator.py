import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Carrega as variáveis de ambiente
load_dotenv(find_dotenv())

# Obtém a chave da API da OpenAI
openai_key = os.getenv("OPENAI_API_KEY")

# Inicializa o cliente OpenAI
client = OpenAI(api_key=openai_key)

def set_response(mensagens, modelo="gpt-4o-mini", temperature=0.5, stream=False):
    # Faz a requisição ao modelo
    completion = client.chat.completions.create(
        model=modelo,
        messages=mensagens,
        temperature=temperature,
        stream=stream
    )
    return completion  # Retorna a resposta completa



# Exibe a resposta da IA
#print(response.choices[0].message.content)
