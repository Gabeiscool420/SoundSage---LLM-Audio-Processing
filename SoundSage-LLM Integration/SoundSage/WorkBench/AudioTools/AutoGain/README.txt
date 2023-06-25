# SoundSage

SoundSage is an innovative audio processing system that integrates automated audio processing tools with a
Language Learning Model (LLM) like OpenAI's ChatGPT.
The system is designed to process audio based on user prompts, automating technical aspects of audio mixing and allowing
users to focus on the creative aspects of their work.


## Table of Contents

1. [AutoGain](#autogain)
2. [Future Tools](#future-tools)
3. [File Management](#file-management)
4. [Error Handling](#error-handling)
5. [User Interface](#user-interface)
6. [Command Handling and Audio Processing](#command-handling-and-audio-processing)
7. [License](#license)

## AutoGain

AutoGain is the first tool integrated into the SoundSage system.
It automates the process of gain staging, setting the clip gain level to industry standards and ensuring a consistent
output for all users.
AutoGain works by taking an input from the user regarding where the audio files are and where the user wants the
processed audio files to be designated for export.

### Modules and Functions

- `audio_analysis.py`: Analyzes the audio prior to processing.
- `audio_processor.py`: Processes the audio based on the analysis.

### API's

- OpenAI's ChatGPT: Used for interpreting user prompts and generating commands for audio processing.

### Sources

- [OpenAI's ChatGPT](https://openai.com/research/chatgpt)

### Licenses

- OpenAI's ChatGPT: [MIT License](https://opensource.org/licenses/MIT)

## Future Tools

SoundSage plans to integrate more tools for automated audio processing, including:

- AutoEQ
- AutoCompressor
- AutoLimiter
- AutoReverb
- AutoDelay
- AutoNoise Reduction
- AutoEnhancer
- AutoStereo Widener
- AutoPitch Corrector
- AutoTime Stretcher

## File Management

SoundSage uses Python scripts to handle file management tasks, including navigating to specified folders, copying files,
and pasting files.

## Error Handling

SoundSage includes error handling scripts to catch exceptions, log them for debugging purposes, and provide useful error
messages to the user.

## User Interface

SoundSage uses a chatbot interface, allowing users to input commands in natural language.
The interface uses OpenAI's LLM to interpret these commands and control the audio processing tools.

## Command Handling and Audio Processing

SoundSage uses natural language processing to interpret user commands and generate a list of commands for audio
processing.
This involves comparing the user's command to a dataset of words and meanings related to specific tasks in the audio
processing field.

## License

SoundSage is licensed under the [MIT License](https://opensource.org/licenses/MIT).
