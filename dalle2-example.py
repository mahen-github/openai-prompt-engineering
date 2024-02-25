from openai import OpenAI

import openai
from openai import AuthenticationError

import os
from dotenv import load_dotenv

load_dotenv()

# client = OpenAI()
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(" output" , completion.choices[0].message)
print(os.environ.get('OPENAI_API_KEY'))

client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a github action for google cloud using OIDC ",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print("here is the url ", image_url)