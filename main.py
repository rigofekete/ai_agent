import os
import sys
from prompt import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types

# we purposefully named this function as generate_content like the genai.Client method, because we are wrapping it with out own implementation and additional arguments 
def generate_content(messages, client, verbose):

    response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            # config will hold additional instructions to the model, as we are doing below
            config=types.GenerateContentConfig(system_instruction=system_prompt)
    )
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print("Response:")
    print(response.text)


def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    verbose = "--verbose" in sys.argv

    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("\n//// AI Code Assistant ////")
        print('\nhow to use this AI agent? type: python main.py "type prompt here" [--verbose]')
        sys.exit(1)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    client = genai.Client(api_key=api_key)

    generate_content(messages, client, verbose)

if __name__ == "__main__":
    main()
