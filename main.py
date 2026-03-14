import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


#  Load and check for Gemini API Key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("API KEY NOT FOUND")


# Set up command line to use user prompt and optional --verbose flag
Chatbot_parser = argparse.ArgumentParser(description="Chatbot")
Chatbot_parser.add_argument("user_prompt", type=str, help="User prompt")
Chatbot_parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = Chatbot_parser.parse_args()


# Obtain user prompt from command line and and get response from Gemini 2.5 Flash model
client = genai.Client(api_key=api_key)
user_prompt_text = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
prompt = client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt_text)

if prompt.usage_metadata == None:
    raise RuntimeError("FAILED API REQUEST")

# If --verbose was included
if args.verbose:
    print(f"User prompt: {user_prompt_text}")
    print(f"Prompt tokens: {prompt.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {prompt.usage_metadata.candidates_token_count}")


print(f"Response:\n{prompt.text}")