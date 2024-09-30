from openai import OpenAI
clint=OpenAI(api_key="test_key")
try:
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user","content": [{"type": "text","text": "what is open ai"}]},])
    
except Exception as e:
    print(f"An error occurred: {e}")