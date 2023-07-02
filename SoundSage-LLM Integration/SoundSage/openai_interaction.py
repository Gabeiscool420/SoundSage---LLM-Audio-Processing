import traceback
import openai
import spacy
import re

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

openai.organization = "YOUR ORG_ID"
openai.api_key = "YOUR OPENAI API-KEY"

def send_input_to_openai(user_input):
    # Send the user's input to the OpenAI API
    try:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=user_input,
            max_tokens=100
        )
    except openai.OpenAIError as e:  # Catch specific OpenAI errors
        print(f"Error in send_input_to_openai: {e}")  # Use the exception object in your print statement
        print(traceback.format_exc())
        return None

    # Return the response from the API
    return response.choices[0].text.strip()


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


daw_extensions = [protools_extension, ableton_extension, garageband_extension, cubase_extension, flstudio_extension,
                  logic_extension, reason_extension, studioone_extension, bitwig_extension, reaper_extension]

daw_extensions = [ext for sublist in daw_extensions for ext in sublist]

# Define a list of audio file extensions
audio_extensions = [".wav", ".mp3", ".flac", ".aiff", ".m4a", ".aac", ".ogg", ".wma", ".alac",
                    ".pcm", ".dsd", ".ape", ".mp2", ".ac3", ".amr", ".au", ".dts", ".mid", ".midi", ".ra", ".rm", ".snd",
                    ".aac", ".caf", ".cda", ".gsm", ".m3u", ".m3u8", ".opus", ".pls", ".sln", ".vox", ".wv"]

def directory_keywords():
    keywords = {"Directory", "Folder", "file folder", "foldre", "driectory", "dircetory", "directroy", "directory", "dir"
                }
    return keywords

# Define a list of subdirectory names to look for
subdirectory_names = ["Audio Files", "Samples", "Recordings", "Mixdowns", "Stems", "Tracks", "Reference Files",
                      "Presets", "Project Backups", "Mix Versions", "Reference Tracks", "Exported Files", "Mastered Files",
                      "Bounced Files", "Processed Files", "Instrumentals", "Vocal Takes", "Projects", "Clip Library",
                      "Sound Design", "Drum Kits", "Vocal Samples", "Instrument Samples", "Ambience", "Guitar DI Tracks",
                      "Audio Loops", "Preset Library", "audio files", "Clips", "Bounces", "Render folder",
                      "Audio assets", "Audio clips", "Audio stems", "Rendered files", "Mixdown"]

def autogain_keywords():
    keywords = {"Gain staging", "gain", "stage", "gain stage", "set", "the", "set the", "Set the Levels",
                "Set the 'autogain_keywords'", "Use Autogain", "automatically", "automate"
                "Line level", "Headroom", "Clipping", "Distortion", "do the gain stage", "Analog gain",
                "Digital gain", "VU meter", "Peak meter", "Metering", "Balance", "signal", "-18 dBFS",
                "-20 dBFS", "-12 dBFS", "-6 dBFS", "0 dBFS", "-24 LUFS", "-23 LUFS", "-18 LUFS", "-16 LUFS",
                "-14 LUFS", "-12 LUFS"
    }
    return keywords


def daw_keywords():
    keywords = {
        "protools": ["ProTools", "Protools", "protools", "pts"] + protools_extension,
        "ableton": ["ableton", "Ableton", "Ablton", "ablton", "Abltn", "abltn", "abl"] + ableton_extension,
        "garageband": ["garageband", "GarageBand", "gb", ".band", "broke man's logic"] + garageband_extension,
        "cubase": ["cubase", "Cubase", "CB", "cub"] + cubase_extension,
        "flstudio": ["flstudio", "FL Studio", "FruityLoops", "fl", "FL", "flp"] + flstudio_extension,
        "logic": ["logic", "Logic Pro", "logicpro", "lp"] + logic_extension,
        "reason": ["reason", "Reason", "rns", ".rns"] + reason_extension,
        "studioone": ["studioone", "Studio One", "s1"] + studioone_extension,
        "bitwig": ["bitwig", "Bitwig Studio", "bw"] + bitwig_extension,
        "reaper": ["reaper", "REAPER", "rpp"] + reaper_extension,
    }
    return keywords


def extract_info_from_response(response):
    # Parse the response using SpaCy
    try:
        doc = nlp(response)
    except ValueError:
        print("Error in extract_info_from_response:")
        print(traceback.format_exc())
        return {}

    # Define a dictionary to store the extracted information
    extracted_keywords = {}

    # Iterate over the sentences in the response
    for sent in doc.sents:
        # If the sentence contains any of the keywords, store the sentence as the extracted information for that keyword
        for keyword in autogain_keywords:
            if keyword in sent.text:
                    extracted_keywords[keyword] = sent.text

        for keyword in directory_keywords():
            if keyword in sent.text:
                extracted_keywords[keyword] = sent.text

        for keyword in subdirectory_names:
            if keyword in sent.text:
                extracted_keywords[keyword] = sent.text

        for keyword in audio_extensions:
            if keyword in sent.text:
                extracted_keywords[keyword] = sent.text

        for keyword in daw_keywords().keys():
            for sub_keyword in daw_keywords()[keyword]:
                if sub_keyword in sent.text:
                    extracted_keywords[keyword] = sent.text

    # Use regular expressions to extract the directory name and DAW project name
    directory_match = re.search(r'in the (.+?) project', response)
    directory_name = None
    if directory_match:
        directory_name = directory_match.group(1)

    # Add the directory name to the extracted information
    extracted_keywords["directory_name"] = directory_name

    # If the prompt contains "daw_keywords" as a keyword, take the relevant keyword
    project_name_found = False
    for keyword in daw_keywords().keys():
        if keyword in response:
            extracted_keywords["project_name"] = keyword
                project_name_found = True
            break

    if not project_name_found:
        extracted_keywords["project_name"] = "No_daw"

        for keyword in daw_keywords():
            if keyword in directory_name:
                extracted_keywords["project_name"] = keyword
                break

        # If no sentence contains the keyword, store the default value as the extracted information for that keyword
        for keyword in autogain_keywords:
            if keyword not in extracted_keywords:
                extracted_keywords[keyword] = None

        for keyword in directory_keywords():
            if keyword not in extracted_keywords:
                extracted_keywords[keyword] = None

        for keyword in daw_keywords().keys():
            if keyword not in extracted_keywords:
                extracted_keywords[keyword] = None

    # Extract the name of the directory and DAW project from the user's input
    directory_match = re.search(r"'(.+?)' Folder", response)
    project_match = re.search(r"'(.+?)' ProTools Project", response)

    # If a match is found, add the extracted name to the extracted_info dictionary
    if directory_match:
        extracted_keywords["directory_name"] = directory_match.group(1)
    if project_match:
        extracted_keywords["project_name"] = project_match.group(1)

    # Return the extracted information
    return extracted_keywords

def confirm_info(extracted_info):
    # Confirm the extracted information with the user
    try:
        for keyword, value in extracted_info.items():
            confirmation = input(f"The {keyword} is {value}. Is this correct? (yes/no): ")
            if confirmation.lower() != "yes":
                return False
    except (KeyError, TypeError) as e:
        print(f"Error in confirm_info: {e}")
        return False

    return True
