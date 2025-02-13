import sys
import os
import streamlit as st
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


# Define o título da aplicação
def pagina_inicial():
    st.header("🤖 Law ChatBot", divider=True)

    mensagens = [{'role': 'system', "content": "Olá, eu sou um assistente virtual que pode te ajudar otimizar seu trabalho como Advogado."},
                 {"role": 'user', "content": "O que é a CLT?"},
                 {"role": "assistant", "content": "Resposta IA"}]
    
    for msg in mensagens:
        chat = st.chat_message(msg["role"])
        chat.markdown(msg["content"])

    prompt = st.chat_input("Digite sua mensagem...")
    if prompt:
        nova_msg = ({"role": "user", "content": prompt})
        
        chat = st.chat_message(nova_msg["role"])
        chat.markdown(nova_msg["content"])
        mensagens.append(msg)

pagina_inicial()