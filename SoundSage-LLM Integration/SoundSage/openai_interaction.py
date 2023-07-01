import openai
import os
import spacy
import re
import autogain_interaction

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

openai.organization = "YOUR ORG-ID"
openai.api_key = "YOUR OPENAI API-KEY"

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

    # Define a list of autogain keywords to look for
    autogain_keywords = ["Gain staging", "Input gain", "Output gain", "Unity gain", "Trim", "Preamp", "Mic preamp",
                         "Line level", "Headroom", "Clipping", "Distortion", "Signal-to-noise ratio", "Analog gain",
                         "Digital gain", "Fader", "VU meter", "Peak meter", "Metering", "Dynamic range", "Overdrive",
                         "Saturation", "Amplification", "Attenuation", "Level matching", "Balanced signal",
                         "Unbalanced signal", "Patchbay", "Mixing console", "Audio interface", "Master bus",
                         "Channel strip", "-18 dBFS (Digital Full Scale)", "-20 dBFS", "-12 dBFS", "-6 dBFS",
                         "0 dBFS", "-24 LUFS", "-23 LUFS", "-16 LUFS", "-14 LUFS", "-12 LUFS"]

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
    def daw_keywords()
    protools_keywords = ["ProTools", "Protools", "protools", "pts", ".ptx"]
    ableton_keywords = ["ableton", "Ableton", "Ablton", "ablton", "Abltn", "abltn", "abl", ".als"]
    garageband_keywords = ["garageband", "GarageBand", "gb", ".band", "brokeman's logic"]
    cubase_keywords = ["cubase", "Cubase", "CB", "cub", ".cpr"]
    flstudio_keywords = ["flstudio", "FL Studio", "FruityLoops", "fl", "FL", "flp", ".flp"]
    logic_keywords = ["logic", "Logic Pro", "logicpro", "lp", ".logic"]
    reason_keywords = ["reason", "Reason", "rns", ".rns"]
    studioone_keywords = ["studioone", "Studio One", "s1", ".song"]
    bitwig_keywords = ["bitwig", "Bitwig Studio", "bw", ".bwp"]
    reaper_keywords = ["reaper", "REAPER", "rpp", ".rpp"]


    # Iterate over the sentences in the response
    for sent in doc.sents:
        # If the sentence contains any of the keywords, store the sentence as the extracted information for that keyword
        for keyword in autogain_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in directory_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in protools_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in ableton_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in garageband_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in cubase_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in flstudio_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in logic_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in reason_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in studioone_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in bitwig_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

        for keyword in reaper_keywords:
            if keyword in sent.text:
                extracted_info[keyword] = sent.text

    # Use regular expressions to extract the directory name and DAW project name
    directory_match = re.search(r'in the (.+?) project', response)
    directory_name = None
    if directory_match:
        directory_name = directory_match.group(1)

    # Add the directory name to the extracted information
    extracted_info["directory_name"] = directory_name

    # If the directory name contains "ProTools" as a keyword, set the project name to "ProTools"
    if daw_keywords in directory_name:
        extracted_info["project_name"] = "ProTools"
    # Otherwise, check if the directory name contains any DAW keyword and set it as the project name
    else:
        for keyword in protools_keywords + ableton_keywords + garageband_keywords \
                + cubase_keywords + flstudio_keywords + logic_keywords + reason_keywords + studioone_keywords \
                + bitwig_keywords + reaper_keywords:
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

    for keyword in protools_keywords + ableton_keywords + garageband_keywords \
            + cubase_keywords + flstudio_keywords + logic_keywords + reason_keywords + studioone_keywords \
            + bitwig_keywords + reaper_keywords:
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
