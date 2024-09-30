from langchain_openai import OpenAI

# import prompt template
from langchain import PromptTemplate
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")


# create the prompt
prompt_template: str = """/
You are a vehicle mechanic, give responses to the following/ 
question: {question}. Do not use technical words, give easy/
to understand responses.
"""

prompt = PromptTemplate.from_template(template=prompt_template)

# format the prompt to add variable values
prompt_formatted_str: str = prompt.format(
    question="Why won't a vehicle start on ignition?")

# instantiate the OpenAI instance
llm = OpenAI(temperature = 0.9,api_key=api_key)

# make a prediction
prediction = llm.predict(prompt_formatted_str)

# print the prediction
print(prediction)
