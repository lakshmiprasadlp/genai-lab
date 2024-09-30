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
Classify the companies given below :
           Microsoft Corporation, Roche Holding AG, Apple Inc, "Amazon.com, Inc,Pfizer Inc, JPMorgan Chase & Co.,Johnson & Johnson, Bank of America Corporation, Industrial and Commercial Bank of China

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
