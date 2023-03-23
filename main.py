import click
from cryptography.fernet import Fernet
import openai
from dotenv import load_dotenv
import os
from firebase_admin import firestore
from firebase import add_question_answer
from session import handle_session

load_dotenv()
encrypted = os.environ.get('APIKey')
encryption_key = os.environ.get('EncryptionKey')
f = Fernet(encryption_key)
decrypted = f.decrypt(encrypted.encode())
openai.api_key = decrypted.decode()

session_id = handle_session()
firestore_db = firestore.client()


@click.group()
def commands():
    pass
# Command only option
# Text to speech

@click.command()
@click.argument("prompt", default="default")
@click.option("--engine", default="text-davinci-003", required=1, help="The engine to use for the AI. (Default: text-davinci-003)")
@click.option("--randomness", default=0.5, required=1, help="The randomness/creativity of the answer. (Default: 0.5)")
@click.option("--word-limit", default=100, help="The word limit of the answer. (Default: 100)")
def ask(prompt, engine, randomness, word_limit):
    """Enter the prompt for the AI to respond to."""
    if prompt == "default":
        click.echo("Command Help AI Thing is running. Use the --prompt option to ask a question.")
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
        add_question_answer(session_id, prompt, response, engine, randomness)


@click.command()
@click.argument("n", default=2)
@click.option("--detailed", default=False, help="Show the details of the previous questions and answers.")
def history(n, detailed):
    """Show the history of previous questions and answers."""
    data_list = list(firestore_db.collection(session_id).order_by('timestamp', direction=firestore.Query.DESCENDING).limit(n).get())
    if detailed:
        for data in data_list:
            question = data.to_dict()['question']
            click.echo(f"\nQuestion: {question}")
            answer = data.to_dict()['answer']
            click.echo(f"Answer: {answer}")
            engine = data.to_dict()['engine']
            click.echo(f"\nEngine: {engine}")
            randomness = data.to_dict()['randomness']
            click.echo(f"\nRandomness: {randomness}")
            timestamp = data.to_dict()['timestamp']
            click.echo(f"\nTimestamp: {timestamp}")
            click.echo("-" * 210)
    else:
        for data in data_list:
            data_dict = data.to_dict()
            question = data_dict['question']
            click.echo(f"\nQuestion: {question}")
            answer = data_dict['answer']
            click.echo(f"\nAnswer: {answer}\n")
            click.echo("-" * 210)


commands.add_command(ask)
commands.add_command(history)


if __name__ == '__main__':
    commands()