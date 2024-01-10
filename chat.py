import fireworks.client
import readline
import re
from rich import print
from rich import pretty
from rich.console import Console

console = Console()
pretty.install()

# jurigged -v chat.py

fireworks.client.api_key = "1KjMT3rFn8IvF4ouKAXwoT8EKIVW7180V2e2TRNAkqMWkvff"

import readline 

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
        if text == "quit":
            break
        out = generate_response(text)
        out = "[bold cyan]" + format(out) + "[/bold cyan]"
        print('\n[yellow]----------------------------------------------------------[/yellow]')
        console.print(out, style="bold yellow")

def generate_response(text):
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
    stop=[],
  )
  for chunk in response_generator:
      if chunk.choices[0].delta.content is not None:
          print(chunk.choices[0].delta.content, end="")


if __name__ == "__main__":
    chat()
