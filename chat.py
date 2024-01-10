import fireworks.client
import readline
import re
import shutil

from rich import print
from rich import pretty
from rich.console import Console

console = Console()
#pretty.install()

color_text = 'white'
color_code = 'cyan'

# jurigged -v chat.py

fireworks.client.api_key = "1KjMT3rFn8IvF4ouKAXwoT8EKIVW7180V2e2TRNAkqMWkvff"

def history_completer(text, state):
    if readline.get_history_length() > 0:
        history = readline.get_history_item(readline.get_current_history_length() - 1)
        if history:
            return history[state]
    return None

readline.parse_and_bind("|: history-complete")
readline.set_completer(history_completer)

def chat():
    while True:
        text = input("chatbot: ")
        generate_response(text)
        print(hr())

def generate_response(text):
  color = color_text
  response_generator = fireworks.client.ChatCompletion.create(
    model="accounts/fireworks/models/llama-v2-34b-code-instruct",
    messages=[{
      "role": "user",
      "content": text,
    }],
    stream=True,
    n=1,
    max_tokens=1000,
    temperature=0.9,
    stop=[]
  )

  for chunk in response_generator:
      if str(chunk.choices[0].delta.content).find('```') > 0:
         print(hr())
      elif chunk.choices[0].delta.content is not None:         
         print (chunk.choices[0].delta.content.replace('``',''), end="")
         #print(chunk.choices[0])

def hr():
    out = ""
    width, height = shutil.get_terminal_size()
    for i in range(width):
        out += '[yellow]_[/yellow]'
    return ('\n' + out + '\n')

if __name__ == "__main__":
    chat()
