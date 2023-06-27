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

def extract_info_from_response(response, keyword, default_value=None):
    # Extract the specified information from the response
    # This is a placeholder function. You would need to implement the actual extraction logic.
    return default_value if keyword not in response else response[keyword]

def confirm_info(keyword, value):
    # Confirm the specified information with the user
    # This is a placeholder function. You would need to implement the actual confirmation logic.
    return value
