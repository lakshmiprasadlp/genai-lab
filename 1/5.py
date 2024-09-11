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
EXPLAIN THE PYTHON CODE GIVEN BELOW
number = int(input("Enter a number:"))
primeFlag = True
for i in range(2, number):
    if number % i == 0:
        primeFlag = False
        break
if primeFlag == True:
    print(number, " is prime.")
else:
    print(number, " is not prime.")


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
