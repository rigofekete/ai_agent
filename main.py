import os
import sys
from prompt import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions, call_function

# we purposefully named this function as generate_content, exactly like the genai.Client method, because we are wrapping it with out own implementation and additional arguments 
def generate_content(messages, client, verbose):

    for i in range(0, 19):

        response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                # config will hold additional instructions to the model, as we are doing below
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
                )
        )
        
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        candidates = response.candidates
        for candidate in candidates:
            messages.append(candidate.content)

        if verbose:
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")

        if not response.function_calls:
            print(f"\nResponse: {response.text}")
            return response.text        

        function_responses = []
        for function_call_part in response.function_calls: 
            function_call_result = call_function(function_call_part, verbose)
            if(
                    not function_call_result.parts or
                    not function_call_result.parts[0].function_response
            ):
                raise Exception("Fatal exception, no content result from call_function() call")
            if verbose:
                print(f"->{function_call_result.parts[0].function_response.response}")
            function_responses.append(function_call_result.parts[0])
            messages.append(function_call_result)

        if not function_responses:
            raise Exception("no function responses generated, exiting.")

    

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
