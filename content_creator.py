import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def create_content(topic, tokens, temperature, model="text-davinci-002"):
    prompt = f"Por favor escribe un articulo corto sobre el tema: {topic}\n\n"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperature
    )
    return response.choices[0].text.strip()

def summarize_text(text, tokens, temperature, model="text-davinci-002"):
    prompt = f"Por favor resume el siguiente texto en español: {text}\n\n"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperature
    )
    return response.choices[0].text.strip()

text = input("Elije un tema para tu articulo: ")
tokens = int(input("Cuántos tokens máximos tendrá tu articulo: "))
temperature = int(input("Del 1 al 10, què tan creativo quieres que sea tu articulo: ")) / 10
created_article = create_content(text, tokens, temperature)
print(created_article)

