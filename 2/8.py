# Ensure to import from the new langchain_openai package
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the LLM with the provided API key and temperature
llm = OpenAI(temperature=0.9, api_key=api_key)

# Define the prompt
prompt = "Suggest a good name for a company that produces socks"

# Use the invoke method to get the response
response = llm.invoke(prompt)

# Print the response
print(response)
