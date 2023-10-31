import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

previous_questions = []
previous_answers = []

def ask_chat_gpt(prompt, model="text-davinci-002"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=1.5
    )
    return response.choices[0].text.strip()

print("Bienvenido a nuestro chatbo básico. Escribe 'salir' cuando quieras terminar")

while True:
    chat_history = ""
    user_question = input("\nTú: ")

    if user_question.lower() == "salir":
        break

    for question, answer in zip(previous_questions, previous_answers):
        chat_history += f"El usuario pregunta: {question}\n"
        chat_history += f"ChatGPT responde: {answer}\n"

    prompt = f"El usuario pregunta: {user_question}\n"
    chat_history += prompt
    gpt_response = ask_chat_gpt(chat_history)

    print(f"{gpt_response}")

    previous_questions.append(user_question)
    previous_answers.append(gpt_response)