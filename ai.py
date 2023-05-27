# ai.py
import openai
import os
import sys

# get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# raise an error if the API key is not set
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# set the API key for the OpenAI API
openai.api_key = api_key

# define a class for the OpenAI chat
class OpenAIChat:
    def __init__(self):
        self.system = None
        self.user = None

    # define a method to role-play the system
    def role_system(self, content):
        self.system = {"role": "system", "content": content}
        return self.system

    # define a method to role-play the user
    def role_user(self, content):
        self.user = {"role": "user", "content": content}
        return self.user

    # define a method to start an OpenAI chat
    def openai_chat(self, messages, max_tokens=10, temperature=0, model="gpt-3.5-turbo"):
        try:
            # create a new chat completion with the OpenAI API
            chat_completion = openai.ChatCompletion.create(
                model=model,
                stream=True,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=messages)

            # initialize an empty string to hold the full message
            full_message = ""

            # consume the generator with a for-loop
            for response in chat_completion:
                chunk = response['choices'][0]['delta'] # type: ignore

                if 'content' in chunk:
                    # concatenate the new piece onto the full message
                    full_message += chunk['content']
                    # print(chunk['content'], end='')
                    sys.stdout.flush()

        except Exception as e:
            print(f"An error occurred while retrieving response: {e}")
            return None

        return full_message