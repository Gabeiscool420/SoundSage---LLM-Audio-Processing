<div align="center">
    <img
      src="SoundSage-LLM Integration/LOGO.png"
      alt="SoundSage Logo"
      title="SoundSage Logo"
      style="display: block; margin: 0 auto; max-width: 30px; width: 15%;">
</div>


# SoundSage---LLM-Audio-Processing-Integration
**TODO:*

- [ ] = exists but is not complete
- [x] = is complete

'>' = Directory(stacks like: >> or >>> etc... for directory within a directory)


## Project Directory:

[>SoundSage](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage) 
- [ ] [*autogain_interaction.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/autogain_interaction.py): This script contains functions for interacting with the AutoGain software. It contains functions for sending commands to the software and handling its responses.
- [ ] [*chatbot_code_writer.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/chatbot_code_writer.py): This script uses the OpenAI API to generate Python code based on the user's input. It modifies a template code to create a new script that can be executed by the system.
- [ ] [*completion_handling.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/completion_handling.py): This script handles the completion of the process. It contains a function for sending a signal to the LLM to respond that the process is complete and a function for checking the new folder to ensure that the process completed successfully.
- [ ] [*error_handling.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/error_handling.py): This script handles errors that might occur during the execution of your application. It also contains functions for providing progress updates to the user.
- [ ] [*file_management.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/file_management.py): This script handles file management tasks. It contains functions for navigating to a specified folder, copying files, and pasting files. 
- [ ] *SoundSage Main* [*main.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/main.py): This is the main script that runs your application. It imports and uses the functions from the other scripts.
- [ ] [*menu_functions.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/menu_functions.py): This script contains functions that get executed when the menu options are selected. For example, it might contain a function for creating a new file when "New.." is selected, a function for saving the current state of the application when "Save As.." is selected, and so on. 
- [ ] [*openai_interaction.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/openai_interaction.py): This script uses the OpenAI API to Parse Keywords and compiles a command list for the system to execute. 
- [ ] [*send_button_functionality.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/send_button_funtionality.py) : This script contains the function that gets executed when the "Send" button is clicked. This function takes the user's input, sends it to the OpenAI API, and displays the response in the chat window.
- [ ] [*template_code.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/template_code.py): This script contains the template code that the chatbot modifies. It is designed to work with the specified files and directories.


  [>>Workbench](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench)

  [>>>PreProcess](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/PreProcess) *This is where the system will always move specified files to before processing.*

  [>>>PostProcess](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/PostProcess) *This is where the system will always move specified files to after processing.*

  [>>>Archive](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/Archive)

  [>>>AudioTools](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools)

[  ](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage)  [>>>>AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain)

- [x] [audio_analysis.py](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain/audio_analysis.py)

- [x] [audio_processor.py](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain/audio_processor.py)

- [x] [main.py](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain/main.py) (this may need to be modified as it is currently a GUI for  AutoGain)

please see [requirements.txt](requirements.txt) for require modules.

## Detailed To-Do List:

1. [**autogain_interaction.py**](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/autogain_interaction.py)
    - [ ] Implement functions for sending commands to the AutoGain software.
    - [ ] Implement functions for handling responses from the AutoGain software.

2. [**chatbot_code_writer.py**](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/chatbot_code_writer.py)
    - [ ] Implement function for generating Python code based on user's input.
    - [ ] Implement function for modifying a template code to create a new script.

3. [**completion_handling.py**](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/completion_handling.py)
    - [ ] Implement function for sending a signal to the LLM to respond that the process is complete.
    - [ ] Implement function for checking the new folder to ensure that the process completed successfully.

4. [**error_handling.py**](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/error_handling.py)
    - [ ] Implement function for handling errors that might occur during the execution of the application.
    - [ ] Implement function for providing progress updates to the user.

5. [**file_management.py**](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/file_management.py)
    - [ ] Implement function for navigating to a specified folder.
    - [ ] Implement function for copying files.
    - [ ] Implement function for pasting files.

6. **SoundSage Main** [**main.py**](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/main.py)
    - [ ] Implement main function that runs the application.
    - [ ] Import and use the functions from the other scripts.

7. [**menu_functions.py**](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/menu_functions.py)
    - [ ] Implement functions that get executed when the menu options are selected.

8. [**openai_interaction.py**](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/openai_interaction.py)
    - [ ] Implement function for sending user's input to the OpenAI API.
    - [ ] Implement function for receiving and processing the response from the OpenAI API.

9. [**send_button_functionality.py**](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/send_button_funtionality.py)
    - [ ] Implement function that gets executed when the "Send" button is clicked.

10. [**template_code.py**](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/template_code.py)
    - [ ] Implement function for modifying the template code based on user's input.

## AutoGain
[AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain) is the first of many audio tools that the [SoundSage](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage) system uses to process audio based on a user's prompt. The [AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain) tool automates gain staging by analyzing the file and either boosting, turning down, or simply doing nothing to the specified file.

# Useful Materials and Sources

This is a list of potential modules/frameworks and tools we could use for SoundSage, if anything material could be used to study and decide how SoundSage will work. 


### 1. [pyAudioProcessing](https://github.com/jsingh811/pyAudioProcessing)

A Python-based library for processing audio data into features (GFCC, MFCC, spectral, chroma) and building Machine Learning models.
This was initially written using Python 3.7, updated several times using Python 3.8 and Python 3.9, and has been tested to work with Python >= 3.6, <3.10.


### 2. [Deep Learning for Audio (DLA)](https://github.com/markovka17/dla)

Lecture and seminar materials for each week are in ./week* folders, see README.md for materials and instructions.
Any technical issues, ideas, bugs in course materials, contribution ideas - add an issue.
The current version of the course is conducted in autumn 2022 at the CS Faculty of HSE.


### 3. [Waveformer (a DNN for low-latency audio processing)](https://github.com/vb000/Waveformer)

This repository provides code for the Waveformer architecture proposed in the paper, Real-Time Target Sound Extraction, presented at ICASSP 2023. 
Waveformer is a low-latency audio processing model implementing streaming inference -- the model process a ~10 ms input audio chunk at each time step, while only looking at past chunks and no future chunks. 
On a Core i5 CPU using a single thread, real-time factors (RTFs) of different model configurations range from 0.66 to 0.94, with an end-to-end latency less than 20 ms.


### 4. [pytorchforaudio](https://github.com/musikalkemist/pytorchforaudio)

Code for the "PyTorch for Audio + Music Processing" series on The Sound of AI YouTube channel.


### 5. [ASP](https://github.com/TUIlmenauAMS/ASP)

Audio Signal Processing (ASP).
It covers a range of utilities for I/O handling and Time-Frequency Decompositions and soon enough audio source separation methods. Currently supported functionallity :
	•	WAV/MP3/AAC Reading and Writing
	•	Time Frequency Methods : MDCT/MDST/PQMF/STFT/FrFFT(Fractional FFT)
	•	Cepstral Analysis : Uniform Discrete Cepstrum
	•	Misc Operations : Bark Scaling, W-Disjoint Orthogonality Measure, Gini Index Sparsity Measure, Time-frequency Masking, Noise to Mask Ratio, Psychoacoustic Model (based on non-linear superposition)
For code usage, please refer to each class. Examples are given inside method or in the "main()" call.

Requirements :
	•	NumPy version '1.10.4' or later
	•	SciPy version '0.17.0' or later (Crucial for avoiding poor reconstruction for the complex PQMF)
	•	cPickle version '1.71' or later
	•	pyglet For audio playback routines


### 6. [Audio Processing](https://github.com/sleekEagle/audio_processing)

Audio processing

mix_noise.py
functions to add noise to a signal provided a Signal to Noise Ratio (SNR).

get_white_noise
returns additive white gausian noise of the provided SNR with respect to the signal

get_noise_from_sound
return noise from an audio file. This noise has the required SNR with respect to the signal


### 7. [Audio DSPy](https://github.com/jatinchowdhury18/audio_dspy)             

audio_dspy is a Python package for audio signal processing tools.
Current tools include:
	•	EQ filter design
	•	Nonlinear Processors
	•	Sine Sweep Tools
	•	Plotting Frequency Responses and Static Curves
	•	Converting transfer functions to minimum or linear phase
	•	Prony's method, and Prony's method with frequency warping
	•	Modal modelling tools


### 8. [Plug and Plai](https://github.com/edreisMD/plugnplai) 

Plug and Plai is an open source library aiming to simplify the integration of AI plugins into open-source language models (LLMs).
It provides utility functions to get a list of active plugins from plugnplai.com directory, get plugin manifests, and extract OpenAPI specifications and load plugins.


### 9. [OpenAI integration with Azure Cognitive-Search for document analysis](https://github.com/Anaig/OpenAI-and-Cognitive-Search)

OpenAI has revolutionized the way we develop applications by providing state-of-the-art machine learning models and making it easy for developers to add AI capabilities to their applications without needing to have an extensive background in data science.
In addition, many of the OpenAI models are available on Azure, where you can get the security capabilities of Microsoft Azure while running the same models as OpenAI. Azure OpenAI offers private networking, regional availability, and responsible AI content filtering.
However, even if OpenAI APIs are very easy to use and integrate, you may have faced some of these limitations:
	•	Format: OpenAI only supports text or json format. If you want to analyze enterprise documents such as PDF, Word, PowerPoint, etc., you need to extract or transform your data.
	•	Source: You cannot directly connect OpenAI to data storages like a database, a SharePoint or a Data Lake.
	•	Token limitation: Depending on the model used, OpenAI requests can use up to 4097 tokens shared between prompt and completion. To analyze longer documents, the text needs to be split into multiple pieces.

What is the added value of using Azure Cognitive Search with OpenAI?
This is where Azure Cognitive Search comes as a great comes as a great complement to Azure OpenAI.
	•	Data Integration: Azure Cognitive Search has connectors to many Data Sources to simplify data ingestion into a search index.
	•	Data transformation: Transforms large undifferentiated file formats into into searchable text. Using the Optical Character Recognition skill, it can even process images.
	•	Split text: The Text Split skill breaks text into chunks of text. You can specify whether you want to break the text into sentences or into pages of a particular length. This skill is useful for the maximum text length requirements in OpenAI.
	•	Translation capabilities: The Text Translation skill evaluates text and returns the text translated to the specified target language. Microsoft Translation API supports more than 70 languages for text translation, while OpenAI has only limited support for a few other languages than English.
Azure OpenAI can offer additional AI enrichment to your Cognitive Search index such as:
	•	Document classification
	•	Document summarization
	•	New insights generation
	•	KPI extraction
	•	Etc.
In this example, we will add summarization capability to the Cognitive Search index using Azure OpenAI.

Requirements
To deploy this project you'll need these Azure resources:
	•	Azure Cognitive Search : S1 tier is recommended
	•	Azure OpenAI: With the text model of your choice
	•	Python Azure Functions: For this project, I used Python 3.9
For the development, it is recommended to use Visual Studio Code and Postman.
For Visual Studio Code, you can install the Azure Function extension and the Azure Function Core Tool.


### 10. [Celery AI](https://github.com/ortegaalfredo/celery-ai)

Multiplatform OpenAI keyboard integration

Description
This is a simple tool that integrates OpenAI ChatGPT and Davinci models by hooking the PC keyboard. It currently works on Linux, Mac and Windows are still buggy. It requires an OpenAI api Key, you can obtain a free evaluation Key from OpenAI by registering and then going to the user settings (https://platform.openai.com/account/api-keys)


<div align="center">
    <img
      src="SoundSage-LLM Integration/LOGO.png"
      alt="SoundSage Logo"
      title="SoundSage Logo"
      style="display: block; margin: 0 auto; max-width: 30px; width: 5%;">
</div>


