import os
import sys
from prompt import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions, call_function
from globals import MAX_ITERS

# we purposefully named this function as generate_content, exactly like the genai.Client method, because we are wrapping it with out own implementation and additional arguments 
def generate_content(messages, client, verbose):

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
    
    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)


    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    if not response.function_calls:
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

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    # we append the wrapped function_responses list as a types.Content because we had to separate the already returned types.Content object parts from function_call_result into the function_responses list. We do these wrappings to keep everything consistent in order to help the model to provide more accurate outputs 
    messages.append(types.Content(role="tool", parts=function_responses))


def main():

    load_dotenv()

    verbose = "--verbose" in sys.argv

    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("\n//// AI Code Assistant ////")
        print('\nhow to use this AI agent? type: python main.py "type prompt here" [--verbose]')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(messages, client, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")

if __name__ == "__main__":
    main()
