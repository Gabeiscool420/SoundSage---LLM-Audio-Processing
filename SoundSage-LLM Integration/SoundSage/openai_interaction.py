import openai
import os

openai.organization = "YOUR ORG-ID"
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

def extract_info_from_response(response, keyword, default_value=None):
    # Extract the specified information from the response
    # This function needs to parse the response and extract the relevant information based on the keyword
    # For simplicity, let's assume the response is a dictionary and we are extracting a value based on the keyword
    return response.get(keyword, default_value)

def confirm_info(keyword, value):
    # Confirm the specified information with the user
    # This function needs to interact with the user to confirm the extracted information
    # For simplicity, let's just print the information and ask for user confirmation
    confirmation = input(f"The {keyword} is {value}. Is this correct? (yes/no): ")
    return confirmation.lower() == "yes"
