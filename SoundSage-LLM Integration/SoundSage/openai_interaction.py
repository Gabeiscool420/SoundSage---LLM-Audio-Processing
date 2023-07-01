import openai
import spacy
import re
import error_handling
from autogain_interaction import autogain_keywords
from file_management import audio_extensions, subdirectory_names
from send_button_functionality import extracted_info

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

openai.organization = "YOUR ORG-ID"

openai.api_key = "YOUR OPENAI API-KEY"

protools_extension = [".ptx"]
ableton_extension = [".als"]
garageband_extension = [".band"]
cubase_extension = [".cpr"]
flstudio_extension = [".flp"]
logic_extension = [".logic"]
reason_extension = [".rns"]
studioone_extension = [".song"]
bitwig_extension = [".bwp"]
reaper_extension = [".rpp"]

def daw_keywords():
    keywords = {
        "protools": ["ProTools", "Protools", "protools", "pts", ".ptx"] + protools_extension,
        "ableton": ["ableton", "Ableton", "Ablton", "ablton", "Abltn", "abltn", "abl", ".als"] + ableton_extension,
        "garageband": ["garageband", "GarageBand", "gb", ".band", "brokeman's logic"] + garageband_extension,
        "cubase": ["cubase", "Cubase", "CB", "cub", ".cpr",] + cubase_extension,
        "flstudio": ["flstudio", "FL Studio", "FruityLoops", "fl", "FL", "flp", ".flp"] + flstudio_extension,
        "logic": ["logic", "Logic Pro", "logicpro", "lp", ".logic"] + logic_extension,
        "reason": ["reason", "Reason", "rns", ".rns"] + reason_extension,
        "studioone": ["studioone", "Studio One", "s1", ".song"] + studioone_extension,
        "bitwig": ["bitwig", "Bitwig Studio", "bw", ".bwp"] + bitwig_extension,
        "reaper": ["reaper", "REAPER", "rpp", ".rpp"] + reaper_extension,
    }
    return keywords


def send_input_to_openai(input):
    # Send the user's input to the OpenAI API
    try:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=input,
            max_tokens=100
        )
    except Exception as e:
        error_handling.handle_error(e)
        return None

    # Return the response from the API
    return response.choices[0].text.strip()


def extract_info_from_response(response):
    # Parse the response using SpaCy
    doc = nlp(response)

    # Define a dictionary to store the extracted information
    extracted_info = {}

    directory_keywords = ["Directory", "Folder", "File", "File management", "Organization", "Hierarchy", "Storage",
                          "Archiving", "Backup", "Naming convention", "File format", "Audio file", "Project file",
                          "Session file", "Export", "Import", "Save", "Load", "Rename", "Copy", "Move", "Delete",
                          "Create", "Duplicate", "Archive", "Batch processing", "Batch export", "Metadata", "Tagging",
                          "Cataloging", "Library", "File browser", "File explorer", "File path", "File location",
                          "File hierarchy", "File structure", "Project management", "Project folder", "Session folder",
                          "Render folder", "Audio assets", "Audio clips", "Audio stems", "Rendered files", "Mixdown",
                          "Mastering", "Version control", "Revision history", "Undo", "Redo", "Collaboration", "Sharing",
                          "Permissions", "Access control", "File transfer", "FTP (File Transfer Protocol)",
                          "Cloud storage", "File synchronization", "Metadata editor", "File conversion", "Crossfading",
                          "Crossfade", "Sample rate conversion", "Bit depth conversion"]



    # Iterate over the sentences in the response
    for sent in doc.sents:
        # If the sentence contains any of the keywords, store the sentence as the extracted information for that keyword
        for keyword in autogain_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in directory_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in subdirectory_names:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in audio_extensions:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in daw_keywords().keys():
            for sub_keyword in daw_keywords()[keyword]:
                if sub_keyword in sent.text:
                    extracted_info[keyword] = sent.text

    # Use regular expressions to extract the directory name and DAW project name
    directory_match = re.search(r'in the (.+?) project', response)
    directory_name = None
    if directory_match:
        directory_name = directory_match.group(1)

    # Add the directory name to the extracted information
    extracted_info["directory_name"] = directory_name

    # If the prompt contains "daw_keywords" as a keyword, take the relevant keyword
    for keyword in daw_keywords().keys():
        if keyword in input():
            extracted_info["project_name"] = keyword
            break
    else:
        extracted_info["project_name"] = "No_daw"

    # Otherwise, check if the directory name contains any DAW keyword and set it as the project name
    else:
        for keyword in daw_keywords():
            if keyword in directory_name:
                extracted_info["project_name"] = keyword
                break

    # If no sentence contains the keyword, store the default value as the extracted information for that keyword
    for keyword in autogain_keywords:
        if keyword not in extracted_info:
            extracted_info[keyword] = None

    for keyword in directory_keywords:
        if keyword not in extracted_info:
            extracted_info[keyword] = None

    for keyword in daw_keywords().keys():
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
