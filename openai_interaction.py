import openai
import os

openai.organization = "YOUR OPENAI ORG-ID "
openai.api_key = os.getenv("YOUR OPENAI API-KEY")

def send_input_to_openai(input):
    # Send the user's input to the OpenAI API
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=input,
        max_tokens=100
    )

    # Return the response from the API
    return response.choices[0].text.strip()
