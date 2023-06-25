# AutoGain-SoundSage
**WORK IN PROGRESS **
Open source Python program for automating Audio Processing using natural language processing. part 1 of a series for automating audio processing tasks, end goal is to create a full set of tools for an AI to use for automating Audio processing for Music, Film, Game and any other possible applications. UI is very basic but 'AutoGain' the original gain-staging application is very functional.

See the AutoGain branch for the Working system that does not involve an LLM, this branch is specific to the LLM Integration. 



# SoundSage

SoundSage is an advanced audio processing system that integrates automated audio tools with a language learning model (LLM) like OpenAI's ChatGPT. The system allows users to prompt a list of commands for audio processing, such as gain staging, balancing, subtractive EQ, noise reduction, and compression.

## AutoGain

AutoGain is the first of many audio tools that the SoundSage system uses to process audio based on a user's prompt. The AutoGain tool automates gain staging by analyzing the file and either boosting, turning down, or simply doing nothing to the specified file.

### Modules Used

- `tkinter`: Used for creating the GUI.
- `PIL`: Used for image processing.
- `audio_analysis`: Custom module for analyzing audio files.
- `audio_processor`: Custom module for processing audio files.
- `ffprobe`: Used for extracting audio file information.
- `ffmpy`: Used for applying gain adjustment to audio files.
- `shutil`: Used for copying files.
- `openai_interaction`: Custom module for interacting with the OpenAI API.

### Functions

- `open_files()`: Opens the file dialog to select audio files.
- `choose_output_directory()`: Opens the directory dialog to select the output directory.
- `begin_process()`: Starts the audio processing.

### APIs

- `OpenAI API`: Used for generating Python code based on user input.

### Sources

- AutoGain scripts: `main.py`, `audio_analysis.py`, `audio_processor.py`

### Licenses

The licensing information for the modules and functions used in the AutoGain scripts is as follows:

- `tkinter`, `PIL`, `shutil`: These are part of the Python Standard Library and are covered by the [Python Software Foundation License](https://docs.python.org/3/license.html).
- `ffprobe`, `ffmpy`: These are licensed under the [GNU General Public License (GPL) version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).
- `audio_analysis`, `audio_processor`, `openai_interaction`: These are custom modules made by SoundSage
