import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.environ.get('APIKey')

model_engine = "text-davinci-003"
prompt = input("Enter your prompt: ")

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)
