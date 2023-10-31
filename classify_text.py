import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def classify_text(text):
    categories = [
        "arte",
        "ciencia",
        "deportes",
        "economia",
        "educacion"
        "entretenimiento",
        "medio ambiente",
        "politica",
        "salud",
        "tecnologia"
    ]
    prompt = f"Por favor clasifica el siguiente text '{text}' en una de estas categorias: {','.join(categories)}. La categoria es: "
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        max_tokens=50,
        temperature=0.5
    )
    return response.choices[0].text.strip()

while True:
    text_to_classify = input("Ingresa un texto: ")
    if text_to_classify.lower() == "salir":
        break

    classification = classify_text(text_to_classify)
    print(classification)


