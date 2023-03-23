import click
from cryptography.fernet import Fernet
import openai
from dotenv import load_dotenv
import os

load_dotenv()
encrypted = os.environ.get('APIKey')
encryption_key = os.environ.get('EncryptionKey')
f = Fernet(encryption_key)
decrypted = f.decrypt(encrypted.encode())
openai.api_key = decrypted.decode()


@click.group()
def commands():
    pass
# Command only option
# Text to speech
# History of last N responses
# 
@click.command()
@click.argument("prompt", default="default")
@click.option("--engine", default="text-davinci-003", required=1, help="The engine to use for the AI. (Default: text-davinci-003)")
@click.option("--randomness", default=0.5, required=1, help="The randomness/creativity of the answer. (Default: 0.5)")
@click.option("--word-limit", default=50, help="The word limit of the answer. (Default: 50)")
def ask(prompt, engine, randomness, word_limit):
    """Prompt for the AI to respond to."""
    if prompt == "default":
        click.echo("Command Help AI Thing is running. Use the --prompt option to prompt the AI to respond to a question.")
    else:
        completions = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=randomness,
        )
        response = completions.choices[0].text
        click.echo(response)

commands.add_command(ask)


if __name__ == '__main__':
    commands()