from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm=OpenAI(temperature=0.9,api_key=api_key)

# Load the .env file

#from langchain import PromptTemplate

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

# instantiate the OpenAI intance
llm = OpenAI(temperature = 0.9)

# make a prediction
prediction = llm.invoke(prompt_formatted_str)

# print the prediction
print(prediction)