import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("API KEY NOT FOUND")

client = genai.Client(api_key=api_key)

user_prompt_text = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

prompt = client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt_text)

if prompt.usage_metadata == None:
    raise RuntimeError("FAILED API REQUEST")

print(f"User prompt: {user_prompt_text}")
print(f"Prompt tokens: {prompt.usage_metadata.prompt_token_count}")
print(f"Response tokens: {prompt.usage_metadata.candidates_token_count}")
print(f"Response:\n{prompt.text}")