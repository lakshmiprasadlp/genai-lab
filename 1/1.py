from openai import OpenAI

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

instruction = """ Summarise the minutes of the meeting given below in 4 bullet points:
                  Car Manufacturing Company

Board of Directors Meeting Minutes

Agenda:
1. Call to Order
2. Approval of Previous Meeting Minutes
3. CEO's Report
4. Financial Report

Meeting Minutes:

1. Call to Order:
   - The meeting was called to order by Bharath Thippireddy.

2. Approval of Previous Meeting Minutes:
   - The minutes of the previous board meeting, held on [Date], were reviewed and approved.

3. CEO's Report:
   - Bharath Thippireddy presented an overview of the company's performance, highlighting key achievements and challenges. Key points discussed include:
     - Sales figures for the last quarter.
     - Progress on cost reduction initiatives.
     - Highlights from recent industry events.
   - The CEO answered questions from board members.

4. Financial Report:
   - The Chief Financial Officer ([CFO's Name]) presented the financial report. Key financial metrics discussed include:
     - Revenue and profit margins.
     - Budget vs. actual expenditure.
     - Cash flow analysis.
   - The board discussed financial performance and the impact on shareholder value.

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
