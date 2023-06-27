# SoundSage - LLM Integration(Text-to-AudioProcessing)

**WORK IN PROGRESS**
Open source Python program for automating Audio Processing using natural language processing. part 1 of a series for automating audio processing tasks, end goal is to create a full set of tools for an AI to use for automating Audio processing for Music, Film, Game and any other possible applications. UI is very basic but 'AutoGain' the original gain-staging application is very functional.

See the AutoGain branch for the Working system that does not involve an LLM, this branch is specific to the LLM Integration. 

# SoundSage

SoundSage is an advanced audio processing system that integrates automated audio tools with a language learning model (LLM) like OpenAI's ChatGPT. The system allows users to prompt a list of commands for audio processing, such as gain staging, balancing, subtractive EQ, noise reduction, and compression.

### How It Works

 The LLM integration process involves the LLM interpreting a user prompt, extracting key information, and using this information to execute a series of actions. The LLM is designed to interpret user prompts and translate them into a series of actions that the system can execute. This process involves a number of scripts that work together to manage files, interact with the OpenAI API, and control the AutoGain tool. These actions include navigating to the specified folder, copying the audio files, pasting them into the "PreProcess" folder, initiating the AutoGain tool, and finally copying the processed files into a new folder. The completion script then sends a signal to indicate that the process is complete and provides the user with information about the location of the processed files. Please see the SoundSage FlowChart** 1 **for a full visualization of the intended process.
 
<img src=“https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/LOGO.png”>

 ## Macro-level Overview of Implementation:

1. **Interpreting User Prompts**: When a user provides a prompt to SoundSage, the LLM analyzes the prompt to understand the user's intent. This involves parsing the prompt, identifying key words and phrases related to audio processing tasks, and extracting any additional information that might be relevant, such as the location of the audio files to be processed.

2. **Generating Commands**: Once the LLM has interpreted the user's prompt, it generates a list of commands for the audio processing tools. These commands are specific to the tasks that the user has requested, such as gain staging, EQ adjustment, or noise reduction. The LLM generates these commands in a format that the audio processing tools can understand and execute.

3. **Executing Commands**: The commands generated by the LLM are passed to the audio processing tools, which execute them in the order they were generated. This involves loading the specified audio files, applying the necessary audio processing tasks, and saving the processed files to the specified location.

4. **Providing Feedback to the User**: After the audio processing tasks have been completed, the LLM generates a response to the user. This response includes information about the tasks that were performed, any changes that were made to the audio files, and the location of the processed files. The response is designed to be easily understood by the user, providing them with a clear and concise summary of the audio processing workflow.

 ## Micro-level Overview of Implementation:

**chatbot_code_writer.py**: This script uses the OpenAI API to generate Python code based on the user's input. It modifies a template code to create a new script that can be executed by the system.

**file_management.py**: This script handles file management tasks. It contains functions for navigating to a specified folder, copying files, and pasting files.

**error_handling.py**: This script handles errors that might occur during the execution of your application. It also contains functions for providing progress updates to the user.

**completion_handling.py**: This script handles the completion of the process. It contains a function for sending a signal to the LLM to respond that the process is complete, and a function for checking the new folder to ensure that the process completed successfully.

**template_code.py**: This script contains the template code that the chatbot modifies. It is designed to work with the specified files and directories.

**main.py**: This is the main script that runs your application. It imports and uses the functions from the other scripts.

**menu_functions.py**: This script contains functions that get executed when the menu options are selected. For example, it might contain a function for creating a new file when "New.." is selected, a function for saving the current state of the application when "Save As.." is selected, and so on.

**send_button_functionality.py**: This script contains the function that gets executed when the "Send" button is clicked. This function takes the user's input, sends it to the OpenAI API, and displays the response in the chat window.

**autogain_interaction.py**: This script contains functions for interacting with the AutoGain software. It contains functions for sending commands to the software and handling its responses.

**audio_analysis.py**: and audio_processor.py: These scripts are part of the AutoGain tool. They handle the analysis and processing of audio files.


## AutoGain

AutoGain is the first of many audio tools that the SoundSage system uses to process audio based on a user's prompt. The AutoGain tool automates gain staging by analyzing the file and either boosting, turning down, or simply doing nothing to the specified file.

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


The current setup is robust and capable of handling complex audio processing tasks. However, there are some trade-offs:

Precision: Depending on the quality of the user's input, the accuracy of the LLM's interpretation and the subsequent commands it generates could vary. There is a potential risk of inaccurate command generation or misinterpretation of the user's intent.

Efficiency: As the system involves multiple scripts and moving parts, the process flow might not be as efficient as it could be with a more streamlined setup. Any lag in communication between scripts or modules could slow down the overall operation.

Resource Consumption: The application may require significant processing power and memory to run efficiently, especially for large audio files or complex audio processing tasks.

 ## Proposed Solution:

**To enhance the algorithm's performance and improve the existing ML algorithm's accuracy:**

Augment the LLM with a domain-specific model: A domain-specific NLP model trained on a corpus of audio processing-related documents and instructions can supplement the LLM to improve the precision of command interpretation and generation. This model could use libraries like Hugging Face's transformers or spaCy for added language processing capabilities.

Optimize Script Interaction: Streamline communication between scripts by creating a central controller script to manage the flow of data and commands. This approach could boost efficiency and speed up operations.

Leverage Efficient Computing Resources: Use optimized ML libraries and compute platforms to reduce resource consumption. Also, consider using cloud-based solutions for scalable and efficient processing.

Augmenting the LLM with a domain-specific model:
a. Data Collection: Gather a substantial corpus of documents related to audio processing. This corpus could include user manuals, online forums, tutorials, and any other text that contains detailed instructions or discussions about audio processing tasks.

b. Preprocessing: Clean the collected data to remove any irrelevant information, and convert it into a format that can be used for model training.

c. Model Training: Use a library like Hugging Face's transformers or spaCy to train a domain-specific model on the preprocessed data.

d. Integration: Integrate the trained model into the LLM, ensuring that the model is invoked when the LLM is interpreting user prompts related to audio processing.

Optimizing Script Interaction:
a. Identify Bottlenecks: Analyze the current script interaction process to identify any areas where inefficiencies may occur. This could involve running performance tests or reviewing the code to understand how data and commands are passed between scripts.

b. Design Central Controller: Design a central controller script that will manage the flow of data and commands between scripts. This script should be designed to handle any issues identified in the bottleneck analysis.

c. Implementation: Rewrite the existing scripts as needed to interact with the central controller, rather than interacting directly with each other. Ensure that the central controller has the necessary functions to manage all required interactions.

d. Testing: Run tests to confirm that the central controller is correctly managing script interactions and that the system is running more efficiently.

Leveraging Efficient Computing Resources:
a. Identify Resource Intensive Tasks: Identify which parts of the application are most resource-intensive. This could be done by monitoring resource usage during typical tasks.

b. Optimize Libraries and Platforms: Review the libraries and platforms used by the application to identify any that could be replaced with more efficient alternatives. For instance, if the application is currently running on a local machine, consider migrating it to a cloud-based solution that can provide more computing power and scalability.

c. Implement Changes: Replace the identified libraries or platforms with the more efficient alternatives. This may involve rewriting parts of the application to work with the new resources.

d. Testing: Run tests to confirm that the application is running more efficiently and that the changes have not introduced any new issues.

### Modules Currently Used in SoundSage and AutoGain

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

## Potential Modules

Here are some potential modules that could be used in the SoundSage LLM integration:

- **transformers**: A Python library for state-of-the-art natural language processing, developed by Hugging Face. It provides pre-trained models for several major LLMs, including OpenAI's GPT-3 and Google's BERT. The library is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

- **scikit-learn**: This is a machine learning library in Python. It features various classification, regression and clustering algorithms, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy. This module is distributed under the [3-Clause BSD license​](https://github.com/scikit-learn/scikit-learn).

- **SoundFile**: This Python package can read and write sound files. File reading/writing is supported for many formats including WAV, FLAC, OGG, and more. This module is licensed under the [BSD 3-Clause License​](https://snyk.io/advisor/python/soundfile)​.

- **spaCy**: A Python library for advanced natural language processing. It provides functionalities for part-of-speech tagging, named entity recognition, and dependency parsing, among others. This could be used to enhance the LLM's ability to interpret user prompts. The library is released under the [MIT License](https://opensource.org/licenses/MIT).

- **nltk (Natural Language Toolkit)**: A Python library for working with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources. This could be used to enhance the LLM's understanding of natural language. The library is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

- **torchaudio**: An audio library for PyTorch. It provides a variety of audio transforms, supports audio I/O, and has dataloaders for common audio datasets. This could be used for loading and saving audio files, as well as performing common audio transformations. The library is released under the [BSD-3-Clause](https://github.com/pytorch/audio)

### Licenses

The licensing information for the modules and functions used in the AutoGain scripts is as follows:

- `tkinter`, `PIL`, `shutil`: These are part of the Python Standard Library and are covered by the [Python Software Foundation License](https://docs.python.org/3/license.html).
- `ffprobe`, `ffmpy`: These are licensed under the [GNU General Public License (GPL) version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).
- AutoGain scripts: `main.py`, `audio_analysis.py`, `audio_processor.py`: These are custom modules made by [SoundSage](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/edit/SoundSage---LLM-Integration).
- `openai api`: this is part of OpenAI's  [open source license](https://github.com/openai/openai-openapi/blob/master/LICENSE).
