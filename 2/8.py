from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")
llm=OpenAI(temperature=0.9,api_key=api_key)


prompt = "Suggest a good name for a company that produces socks"



print(llm(prompt))

#get a deterministic response with temp = 0



#generate 5 creative responses using the prompt repeatedly



responses = llm.generate([prompt]*5)



for name in responses.generations:
  print(name[0].text)