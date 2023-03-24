import click
from cryptography.fernet import Fernet
import openai
from dotenv import load_dotenv
import os
from firebase_admin import firestore
from firebase import save_data
from session import handle_session

# Fetching and decrypting the API key
load_dotenv()
encrypted = os.environ.get('APIKey')
encryption_key = os.environ.get('EncryptionKey')
f = Fernet(encryption_key)
decrypted = f.decrypt(encrypted.encode())
openai.api_key = decrypted.decode()

# Fetching the session ID and initializing the Firestore database
session_id = handle_session()
firestore_db = firestore.client()


@click.group()
def commands():
    pass


@click.command()
@click.argument("prompt", default="default")
@click.option("--engine", default="text-davinci-003", required=1, help="The engine to use for the AI. (Default: text-davinci-003)")
@click.option("--randomness", default=0.5, required=1, help="The randomness/creativity of the answer. (Default: 0.5)")
@click.option("--word-limit", default=100, help="The word limit of the answer. (Default: 100)")
@click.option("--top-p", default=1, help="The top_p parameter of the OpenAI API. (Default: 1)")
@click.option("--frequency-penalty", default=0, help="The frequency_penalty parameter of the OpenAI API. (Default: 0)")
@click.option("--presence-penalty", default=0, help="The presence_penalty parameter of the OpenAI API. (Default: 0)")
@click.option("--best-of", default=1, help="The best_of parameter of the OpenAI API. (Default: 1)")
def ask(prompt, engine, randomness, word_limit, top_p, frequency_penalty, presence_penalty, best_of):
    """Enter the prompt for the AI to respond to."""
    if prompt == "default":
        click.echo("Command Help AI Thing is running. Use the --prompt option to ask a question.")
    else:
        completions = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=randomness,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            best_of=best_of,
        )

        response = completions.choices[0].text
        click.echo(response)
        save_data(session_id, prompt, response, engine, randomness)


@click.command()
@click.argument("n", default=10)
@click.option("--detailed", default=False, help="Show the details of the previous questions and answers.")
def history(n, detailed):
    """Show the history of previous questions and answers."""
    data_list = list(firestore_db.collection(session_id).order_by('timestamp', direction=firestore.Query.DESCENDING).limit(n).get())
    if detailed:
        q_count = 1
        for data in data_list:
            question = data.to_dict()['question']
            click.echo(f"\nQ{q_count}: {question}")

            answer = data.to_dict()['answer']
            click.echo(f"\nAnswer: {answer}")

            engine = data.to_dict()['engine']
            click.echo(f"\nEngine: {engine}")

            randomness = data.to_dict()['randomness']
            click.echo(f"\nRandomness: {randomness}")

            timestamp = data.to_dict()['timestamp']
            click.echo(f"\nTimestamp: {timestamp}")
            click.echo("-" * 210)
            q_count += 1
    else:
        q_count = 1
        for data in data_list:
            data_dict = data.to_dict()
            question = data_dict['question']
            click.echo(f"\nQ{q_count}: {question}")

            answer = data_dict['answer']
            click.echo(f"\nAnswer: {answer}\n")
            click.echo("-" * 210)
            q_count += 1


commands.add_command(ask)
commands.add_command(history)


if __name__ == '__main__':
    commands()
