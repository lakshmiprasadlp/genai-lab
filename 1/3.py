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
Given a set of Social Media Posts below, analyse the sentiment of each and classify it as either positive, negative, or neutral. Provide a brief explanation for your classification

1. Just got my hands on the new XPhone - absolutely loving the camera and battery life! 📸🔋 #TechLove
2. Disappointed with the XPhone. Its pricey and not much different from the last model. Expected more. 😕 #TechTalk
3. XPhones latest update is a game-changer for mobile gaming. The graphics are just incredible! 🎮💯
4. Cant believe I waited this long for the XPhone... its underwhelming and overpriced. Back to my old phone, I guess. 😒
5. The XPhone has exceeded my expectations. Fast, sleek, and the new AI features are a standout! 🚀 #Innovation
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
