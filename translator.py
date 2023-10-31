import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def translate_text(text, language):
    prompt = f"Traduce el texto '{text}' al {language}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        max_tokens=100,
        temperature=0.5
    )
    return response.choices[0].text.strip()

my_text = input("Escribe el texto que quieres traducir: ")
my_language = input("A qué idioma lo quieres traducir: ")
translation = translate_text(my_text, my_language)
print(translation)