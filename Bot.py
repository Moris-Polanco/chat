import os
from unittest.util import _MAX_LENGTH
import openai
import streamlit as st
openai.api_key = os.getenv('OPENAI_API_KEY')


start_sequence = "\nAI:"
restart_sequence = "\n\nPerson:"


session_prompt = "{
  "model": "text-davinci-002",
  "prompt": "Lo que sigue es una conversación con un asistente de AI. El asistente es un experto en vinos, servicial, creativo, inteligente y muy amable.\n\nHumano: Hola, ¿quién eres?\nAI: Hola, soy un asistente de IA especializado en vinos. Estoy aquí para ayudarle con cualquier pregunta que pueda tener sobre el vino. Por favor, hágame saber si hay algo en lo que pueda ayudarle.\nHumano: ¿Qué es un vino tinto?\nAI: El vino tinto es un tipo de vino que se hace a partir de uvas rojas o negras. generalmente, el vino tinto tiene un sabor más fuerte y robusto que el vino blanco.\nAI: ¿Le gustaría saber más sobre el vino tinto?\nHuman: Sí\nAI: En general, el vino tinto se caracteriza por su sabor más fuerte y robusto. Sin embargo, existen diferentes tipos y estilos de vino tinto, por lo que puede haber algunos que sean más afines a su paladar. ¿Le gustaría que le recomiende algunos vinos tintos para probar?\nHuman: Sí\nAI: De acuerdo. Algunos de los vinos tintos que puede probar son el Merlot, el Cabernet Sauvignon, el Pinot Noir y el Zinfandel. ¿Hay alguno de estos que le llame la atención?\nHuman: Pinot Noir\nAI: El Pinot Noir es un tipo de vino tinto muy popular. Se caracteriza por su sabor afrutado y liviano. ¿Le gustaría saber más sobre el Pinot Noir?\nHuman: Sí\nAI: El Pinot Noir es un vino tinto ligero y afrutado. Tiene\nHuman: \nAI: El Pinot Noir es un vino tinto ligero y afrutado. Tiene un sabor a frutas maduras, como la ciruela y la frambuesa, y suele tener un cuerpo liviano. ¿Le gustaría probar un Pinot Noir?\nHuman: ¿A qué temperatura se debe servir el vino blanco?\nAI:  El vino blanco se sirve mejor en una temperatura entre 8-10°C.\nHuman: ",
  "temperature": 0.9,
  "max_tokens": 150,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0.6,
  "stop": [" Human:", " AI:"]
}"
def mises(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.7,
        # max_length=1024,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
