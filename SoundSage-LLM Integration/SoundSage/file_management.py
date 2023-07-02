import os
import glob
import shutil
import traceback

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

# Define a list of subdirectory names to look for
subdirectory_names = ["Audio Files", "Samples", "Recordings", "Mixdowns", "Stems", "Tracks", "Reference Files",
                      "Presets", "Project Backups", "Mix Versions", "Reference Tracks", "Exported Files", "Mastered Files",
                      "Bounced Files", "Processed Files", "Instrumentals", "Vocal Takes", "Projects", "Clip Library",
                      "Sound Design", "Drum Kits", "Vocal Samples", "Instrument Samples", "Ambience", "Guitar DI Tracks",
                      "Audio Loops", "Preset Library", "audio files", "Clips", "Bounces", "Render folder",
                      "Audio assets", "Audio clips", "Audio stems", "Rendered files", "Mixdown"]


def confirm_directory(directory_name):
    # Define a list to store the confirmed directory paths
    confirmed_directory_paths = []
    try:
        # Iterate over the directory paths
        for directory_path in directory_name:
            # If the directory contains a DAW project file, add it to the list of confirmed directory paths
            for ext_list in daw_extensions:
                for ext in ext_list:
                    if glob.glob(os.path.join(directory_path, "*" + ext)):
                        confirmed_directory_paths.append(directory_path)
                        break  # If a matching file is found, no need to check other extensions
                else:
                    continue  # Continue if the inner loop wasn't broken
                break  # Inner loop was broken, break the outer loop
            else:  # This else clause corresponds to the for loop, not the if statement
                # Check if the directory contains a subdirectory with a matching name that contains an audio file
                for subdirectory_name in subdirectory_names:  # Use a different variable name here
                    subdirectory_path = os.path.join(directory_path, subdirectory_name)
                    if os.path.isdir(subdirectory_path):
                        for ext in audio_extensions:
                            if glob.glob(os.path.join(subdirectory_path, "*" + ext)):
                                confirmed_directory_paths.append(subdirectory_path)
                                break  # If a matching file is found, no need to check other extensions
    except OSError as e:
        print(f"Error in confirm_directory: {e}")
        print(traceback.format_exc())

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
    try:
        # Walk through the file system starting from the project directory
        for dirpath, dirnames, filenames in os.walk(project_directory):
            # If the directory name matches any of the possible names, return its path
            if any(name in dirpath for name in subdirectory_names):
                return dirpath
    except OSError as e:
        print(f"Error in find_audio_files_directory: {e}")
        print(traceback.format_exc())
    # If no matching directory is found, return None
    return None


def copy_files_to_preprocess(directory_path):
    # Define the destination path
    destination_path = "/SoundSage---LLM-Audio-Processing/SoundSage-LLM Integration/SoundSage/WorkBench/PreProcess"

    # If the directory contains an audio file, copy it to the destination path
    try:
        for filename in os.listdir(directory_path):
            if any(filename.endswith(ext) for ext in audio_extensions):
                shutil.copy2(os.path.join(directory_path, filename), os.path.join(destination_path, filename))
    except (shutil.Error, OSError) as e:
        print(f"Error in copy_files_to_preprocess: {e}")
        print(traceback.format_exc())
