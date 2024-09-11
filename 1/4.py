from openai import OpenAI

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

instruction = """
GENERATE 3 RECIPES FOR BAKING A CAKE
"""

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user","content": [{"type": "text","text": instruction}]},],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#print(response)
print(response.choices[0].message.content)
