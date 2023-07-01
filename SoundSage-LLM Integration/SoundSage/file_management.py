import os
import glob
import time
import shutil
import error_handling

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

def find_directory(directory_name):
    # Define the root directory to start the search from
    root_dir = "/"

    # Define a list to store the directory paths
    directory_paths = []

    # Walk through the file system
    try:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # If the directory name matches the specified directory name, add the directory path to the list
            if os.path.basename(dirpath) == directory_name:
                directory_paths.append(dirpath)
    except Exception as e:
        error_handling.handle_error(e)

    # Return the list of directory paths
    return directory_paths

def confirm_directory(directory_paths):
    daw_extensions = protools_extension + ableton_extension + garageband_extension + cubase_extension + \
                     flstudio_extension + logic_extension + reason_extension + studioone_extension + bitwig_extension + \
                     reaper_extension


    # Define a list of audio file extensions
    audio_extensions = [".wav", ".mp3", ".flac", ".aiff", ".m4a", ".aac", ".ogg", ".wma", ".alac", ".pcm", ".dsd",
                        ".ape", ".mp2", ".ac3", ".amr", ".au", ".dts", ".mid", ".midi", ".ra", ".rm", ".snd", ".aac",
                        ".caf", ".cda", ".gsm", ".m3u", ".m3u8", ".opus", ".pls", ".sln", ".vox", ".wv"]

    # Define a list of subdirectory names to look for
    subdirectory_names = ["Audio Files", "MIDI Files", "Samples", "Recordings", "Mixdowns", "Stems", "Tracks",
                          "Session Notes", "Lyrics", "Reference Files", "Presets", "Project Backups", "Tempo Maps",
                          "Automation", "Markers", "FX Chains", "Plugin Settings", "Mix Versions", "Reference Tracks",
                          "Reference Videos", "Project Documentation", "Exported Files", "Mastered Files",
                          "Bounced Files", "Processed Files", "Instrumentals", "Vocal Takes", "Editing", "Arrangement",
                          "Session Templates", "Cues", "Revisions", "Projects", "Collaborations", "Session Logs",
                          "Clip Library", "Effects Library", "Instrument Library", "Sound Design", "Drum Kits",
                          "Vocal Samples", "Instrument Samples", "Ambience", "Guitar DI Tracks", "Synth Patches",
                          "Audio Loops", "Preset Library"]

    # Define a list to store the confirmed directory paths
    confirmed_directory_paths = []

    # Iterate over the directory paths
    for directory_path in directory_paths:
        # If the directory contains a DAW project file, add it to the list of confirmed directory paths
        if any(glob.glob(os.path.join(directory_path, "*" + ext)) for ext in daw_extensions):
            confirmed_directory_paths.append(directory_path)
        # Otherwise, check if the directory contains a subdirectory with a matching name that contains an audio file
        else:
            for subdirectory_name in subdirectory_names:
                subdirectory_path = os.path.join(directory_path, subdirectory_name)
                if os.path.isdir(subdirectory_path) and any(glob.glob(os.path.join(subdirectory_path, "*" + ext)) for ext in audio_extensions):
                    confirmed_directory_paths.append(subdirectory_path)

    # If there are multiple confirmed directory paths, return the one that was modified most recently
    if len(confirmed_directory_paths) > 1:
        return max(confirmed_directory_paths, key=os.path.getmtime)

    # If there is only one confirmed directory path, return it
    elif confirmed_directory_paths:
        return confirmed_directory_paths[0]

    # If there are no confirmed directory paths, return None
    else:
        return None

def find_audio_files_directory(project_directory):
    # Define a list of possible names for the audio files directory
    audio_files_directory_names = ["Audio Files", "Stems", "Clips"]

    # Walk through the file system starting from the project directory
    for dirpath, dirnames, filenames in os.walk(project_directory):
        # If the directory name matches any of the possible names, return its path
        if os.path.basename(dirpath) in audio_files_directory_names:
            return dirpath

    # If no matching directory is found, return None
    return None

def copy_files_to_preprocess(directory_path, destination_path):
    # Define a list of audio file extensions
    audio_extensions = [".wav", ".mp3", ".flac", ".aiff", ".m4a", ".aac", ".ogg", ".wma", ".alac", ".pcm", ".dsd",
                        ".ape", ".mp2", ".ac3", ".amr", ".au", ".dts", ".mid", ".midi", ".ra", ".rm", ".snd", ".aac",
                        ".caf", ".cda", ".gsm", ".m3u", ".m3u8", ".opus", ".pls", ".sln", ".vox", ".wv"]

    # If the directory contains an audio file, copy it to the destination path
    for filename in os.listdir(directory_path):
        if any(filename.endswith(ext) for ext in audio_extensions):
            try:
                shutil.copy2(os.path.join(directory_path, filename), destination_path)
            except Exception as e:
                error_handling.handle_error(e)

