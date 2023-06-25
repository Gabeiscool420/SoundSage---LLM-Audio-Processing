import openai
import os

openai.organization = "org-PlTiAlDynKPPj6WZZZtze1F4"
openai.api_key = os.getenv("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")

def send_input_to_openai(input):
    # Send the user's input to the OpenAI API
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=input,
        max_tokens=100
    )

    # Return the response from the API
    return response.choices[0].text.strip()
