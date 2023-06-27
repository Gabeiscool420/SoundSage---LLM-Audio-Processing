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

def extract_info_from_response(response):
    # Parse the response using SpaCy
    doc = nlp(response)

    # Define a dictionary to store the extracted information
    extracted_info = {}

    # Define a list of keywords to look for
    keywords = ["Gain-Stage", "folder", "all", "Clips", "ProTools Project"]

    # Iterate over the sentences in the response
    for sent in doc.sents:
        # If the sentence contains any of the keywords, store the sentence as the extracted information for that keyword
        for keyword in keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        # Use SpaCy's named entity recognition to extract the directory name
        for ent in sent.ents:
            if ent.label_ == "WORK_OF_ART":
                extracted_info["directory_name"] = ent.text

    # If no sentence contains the keyword, store the default value as the extracted information for that keyword
    for keyword in keywords:
        if keyword not in extracted_info:
            extracted_info[keyword] = None

    # Return the extracted information
    return extracted_info

def confirm_info(keyword, value):
    # Confirm the specified information with the user
    # This function needs to interact with the user to confirm the extracted information
    # For simplicity, let's just print the information and ask for user confirmation
    confirmation = input(f"The {keyword} is {value}. Is this correct? (yes/no): ")
    return confirmation.lower() == "yes"
