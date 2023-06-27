#﻿AutoGain by SoundSage Instructions

## AutoGain  🦉

AutoGain is the first tool integrated into the SoundSage system.
It automates the process of gain staging, setting the clip gain level to industry standards and ensuring a consistent
output for all users.
AutoGain works by taking input from the user regarding where the audio files are and where the user wants the
processed audio files to be designated for export.


### Step 1: Install Python


Visit the [Python website](https://www.python.org)
[Download Python3.10](https://www.python.org/downloads/)
Run the installer and follow the installation instructions, making sure to check the box that says "Add Python to PATH" during installation.

### Step 2: Install PyCharm


Visit the [PyCharm website](https://www.jetbrains.com/pycharm/).
Download the [Community Edition of PyCharm](https://www.jetbrains.com/pycharm/download/).
Run the installer and follow the installation instructions.

### Step 3: Set up the project


Unzip the folder containing the Python scripts and the logo.
Open PyCharm.
Click on "Open" and select the unzipped folder with the Python scripts.
PyCharm will automatically detect the virtual environment (venv) in the project folder.

### Step 4: Install required packages


Open Terminal 
Individually copy and paste the following commands into terminal to install the required packages, press enter to run the command:

- `pip install librosa`
- `pip install numpy`
- `pip install pyloudnorm`
- `pip install tkinter`
- `pip install Pillow`

*note: If pip doesn’t work try pip3, if that doesn't work try: 
- `python3 -m pip install --upgrade pip` 
If none of this works it is because you need to install pip by putting this command in the terminal: 
- `“curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py”`: Now try installing the required packages above.

### Step 5: Run the program


In the PyCharm Project panel, locate the Python script file named main.py (this file contains the script for the AutoGain program).
Right-click the main.py file and select "Run 'main'" from the context menu. This will start the AutoGain program.


Once you have the AutoGain UI open you can select the files you want to be processed, and the directory you would like to export them to, once that is complete press begin and the processing will commence. When the process is finished navigate to the chosen export directory and import them in to the DAW. analyze with WLMmeter or VUmeter of your choice!

## Modules and Functions

- `audio_analysis.py`: Analyzes the audio prior to processing.
- `audio_processor.py`: Processes the audio based on the analysis.


## User Interface

AutoGain has a simple UI for choosing files and the intended destination directory and a button to click to begin processing.## Future Tools

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
