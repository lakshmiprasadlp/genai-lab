from openai import OpenAI

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)



messages = [ {'role':'system', 'content':"You are a Math Tutor"}]
user_messages = ['Explain what is PI', 'Summarize this in two bullet points']



for each_message in user_messages:
  user_dict = {'role': 'user', 'content':[{'type': 'text', 'text': each_message}]}
  messages.append(user_dict)

  response = client.chat.completions.create(
        model="gpt-3.5-turbo",
  messages=messages)

  assist_dict ={'role':'assistant', 'content': [{'type': 'text', 'text': response.choices[0].message.content}]}
  messages.append(assist_dict)

  print(response.choices[0].message.content)