import os
import openai
import spacy
from dotenv import load_dotenv

# pip install python-dotenv
# pip install openai
# pip install spacy
# python -m spacy download es_core_news_md

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

model = "text-davinci-002"
prompt = "Cuenta una historia breve."

response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    n=1,
    # temperature=1,
    max_tokens=100
)

text_generated = response.choices[0].text.strip()
print(text_generated)

#for idx, option in enumerate(response.choices):
#    text_generated = option.text.strip()
#    print(f"Respuesta {idx + 1} : {text_generated}\n")

model_spacy = spacy.load("es_core_news_md")