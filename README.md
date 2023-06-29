<div align="center">
    <img
      src="SoundSage-LLM Integration/LOGO.png"
      alt="SoundSage Logo"
      title="SoundSage Logo"
      style="display: block; margin: 0 auto; max-width: 30px; width: 10%;">
</div>

# SoundSage LLM Integration (text-to-audio-processing)

**WORK IN PROGRESS**

#### Welcome to SoundSage!🦉 

*If you are reading this then you are about to be one of the very few to know of our journey!* &#128640; 

We are on a mission to create the world's first AI-based audio processing suite. The tools use AI to analyze and process audio files, improving the quality and efficiency of the audio processing workflow.

- **User-friendly interface**: The system will feature a simple and intuitive chat interface, making it easy for users to navigate and use the tool by simply prompting SoundSage.🦉
- **Efficient workflow**: The tools will be designed to streamline the audio processing workflow, allowing users to process audio files quickly and easily.🛠
- **Operating Environment**: The product is designed to operate in a standard computing environment. It requires a computer with sufficient processing power to run the AI algorithms and enough storage space to store the audio files.


Open-source Python program for automating Audio Processing using natural language processing. part 1 of a series for automating audio processing tasks, the end goal is to create a full set of tools for an AI to use for automating Audio processing for Music, Film, Game and any other possible applications. UI is very basic but [AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain) the original gain-staging application is very functional.

See the [AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain) branch for the Working system that does not involve an LLM, this branch is specific to the LLM Integration. 

# SoundSage🦉

[SoundSage](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage) is an advanced audio processing system that integrates automated audio tools with a language learning model (LLM) like [OpenAI API](https://openai.com/policies/terms-of-use). The system allows users to prompt a list of commands for audio processing, such as gain staging, balancing, subtractive EQ, noise reduction, and compression.

## Project Overview

 The LLM integration process involves the LLM interpreting a user prompt, extracting key information, and using this information to execute a series of actions. The LLM is designed to interpret user prompts and translate them into a series of actions that the system can execute. This process involves a number of scripts that work together to manage files, interact with the [OpenAI API](https://openai.com/policies/terms-of-use), and control the [AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain) tool. These actions include navigating to the specified folder, copying the audio files, pasting them into the "[PreProcess](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/PreProcess)" folder, initiating the [AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain) tool, and finally copying the processed files into a new folder. The completion script then sends a signal to indicate that the process is complete and provides the user with information about the location of the processed files. Please see the [SoundSage FlowChart](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/assets/130602253/57c1aedb-5e18-4ea4-84c8-56a0aa21bd12) for a full visualization of the intended process.
 
![SoundSage - AutoGain Workflow](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/assets/130602253/57c1aedb-5e18-4ea4-84c8-56a0aa21bd12)

### How it Works:

1. **Interpreting User Prompts**: When a user provides a prompt to [SoundSage](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage), the LLM analyzes the prompt to understand the user's intent. This involves parsing the prompt, identifying keywords and phrases related to audio processing tasks, and extracting any additional information that might be relevant, such as the location of the audio files to be processed.

2. **Generating Commands**: Once the LLM has interpreted the user's prompt, it generates a list of commands for the audio processing tools. These commands are specific to the tasks that the user has requested, such as gain staging, EQ adjustment, or noise reduction. The LLM generates these commands in a format that the audio processing tools can understand and execute.

3. **Executing Commands**: The commands generated by the LLM are passed to the audio processing tools, which execute them in the order they were generated. This involves loading the specified audio files, applying the necessary audio processing tasks, and saving the processed files to the specified location.

4. **Providing Feedback to the User**: After the audio processing tasks have been completed, the LLM generates a response to the user. This response includes information about the tasks that were performed, any changes that were made to the audio files, and the location of the processed files. The response is designed to be easily understood by the user, providing them with a clear and concise summary of the audio processing workflow.

### Code Documentation:
**please see* [SoundSage To Do List](TODO.md)

[*chatbot_code_writer.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/chatbot_code_writer.py): This script uses the [OpenAI API](https://openai.com/policies/terms-of-use) to generate Python code based on the user's input. It modifies a template code to create a new script that can be executed by the system.

[*openai_interaction.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/openai_interaction.py): This script uses the [OpenAI API](https://openai.com/policies/terms-of-use) to Parse Keywords and compiles a command list for the system to execute.

[*file_management.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/file_management.py): This script handles file management tasks. It contains functions for navigating to a specified folder, copying files, and pasting files.

[*error_handling.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/error_handling.py): This script handles errors that might occur during the execution of your application. It also contains functions for providing progress updates to the user.

[*completion_handling.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/completion_handling.py): This script handles the completion of the process. It contains a function for sending a signal to the LLM to respond that the process is complete and a function for checking the new folder to ensure that the process completed successfully.

[*template_code.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/template_code.py): This script contains the template code that the chatbot modifies. It is designed to work with the specified files and directories.

*SoundSage Main* [*main.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/main.py): This is the main script that runs your application. It imports and uses the functions from the other scripts.

[*menu_functions.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/menu_functions.py): This script contains functions that get executed when the menu options are selected. For example, it might contain a function for creating a new file when "New.." is selected, a function for saving the current state of the application when "Save As.." is selected, and so on.

[*send_button_functionality.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/send_button_funtionality.py) : This script contains the function that gets executed when the "Send" button is clicked. This function takes the user's input, sends it to the [OpenAI API](https://openai.com/policies/terms-of-use), and displays the response in the chat window.

[*autogain_interaction.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/autogain_interaction.py): This script contains functions for interacting with the [AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain) software. It contains functions for sending commands to the software and handling its responses.

## AutoGain

[AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain) is the first of many audio tools that the [SoundSage](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage) system uses to process audio based on a user's prompt. The AutoGain tool automates gain staging by analyzing the file and either boosting, turning down, or simply doing nothing to the specified file.

*AutoGain Main* [*main.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain/main.py),[*audio_analysis.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain/audio_analysis.py) and [*audio_processor.py*](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/blob/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain/audio_processor.py): These scripts are part of the AutoGain tool. They handle the analysis and processing of audio files.

## Getting Started

To get started with SoundSage, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the main script to start the application.

### Prerequisites

Before you can use SoundSage, you need to have the following software installed on your computer:

- Python 3.8 or later
- pip (Python package installer)

### Installation

1. Clone the repository:

```bash
- `git clone https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing.git`

a). Navigate to the cloned repository:
- `cd SoundSage---LLM-Audio-Processing`


## Contributing Guidelines

Thank you for considering contributing to [SoundSage](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage)! Anyone can contribute we just ask you to adhere to our guidelines!
For Contribution Guidelines please see [CONTRIBUTING.md](CONTRIBUTING.md). If everything looks good to you then feel free to take a stab at the [SoundSage to-do list](TODO.md)! please leave a comment and document any changes you have made as well as cite any code you may have borrowed! 

- Fork the repository.
- Create a new branch for your changes.
- Make your changes in your branch.
- Submit a pull request with your changes.

*Please make sure to update tests as appropriate.*

##### Cheers! :)
 *The SoundSage Team*

## Future Tools

### SoundSage plans to integrate more tools for automated audio processing, including:

- `AutoEQ`
- `AutoDelay`
- `AutoReverb`
- `AutoLimiter`
- `AutoEnhancer`
- `AutoCompressor`
- `AutoStereo Widener`
- `AutoTime Stretcher`
- `AutoPitch Corrector`
- `AutoNoise Reduction`

Precision: Depending on the quality of the user's input, the accuracy of the LLM's interpretation and the subsequent commands it generates could vary. There is a potential risk of inaccurate command generation or misinterpretation of the user's intent.

Efficiency: As the system involves multiple scripts and moving parts, the process flow might not be as efficient as it could be with a more streamlined setup. Any lag in communication between scripts or modules could slow down the overall operation.

Resource Consumption: The application may require significant processing power and memory to run efficiently, especially for large audio files or complex audio processing tasks.

 ## Proposed Solution:

**To enhance the algorithm's performance and improve the existing ML algorithm's accuracy:**

Augment the LLM with a domain-specific model: A domain-specific NLP model trained on a corpus of audio processing-related documents and instructions can supplement the LLM to improve the precision of command interpretation and generation. This model could use libraries like [Hugging Face](https://huggingface.co/terms-of-service)'s transformers or [spaCy](https://spacy.io/api/doc) for added language processing capabilities.

Optimize Script Interaction: Streamline communication between scripts by creating a central controller script to manage the flow of data and commands. This approach could boost efficiency and speed up operations.

Leverage Efficient Computing Resources: Use optimized ML libraries and compute platforms to reduce resource consumption. Also, consider using cloud-based solutions for scalable and efficient processing.

### Augmenting the LLM with a domain-specific model:

a. Data Collection: Gather a substantial corpus of documents related to audio processing. This corpus could include user manuals, online forums, tutorials, and any other text that contains detailed instructions or discussions about audio processing tasks.

b. Preprocessing: Clean the collected data to remove any irrelevant information, and convert it into a format that can be used for model training.

c. Model Training: Use a library like [Hugging Face](https://huggingface.co/terms-of-service)'s transformers or [spaCy](https://spacy.io/api/doc) to train a domain-specific model on the preprocessed data.

d. Integration: Integrate the trained model into the LLM, ensuring that the model is invoked when the LLM is interpreting user prompts related to audio processing.

### Optimizing Script Interaction:
a. Identify Bottlenecks: Analyze the current script interaction process to identify any areas where inefficiencies may occur. This could involve running performance tests or reviewing the code to understand how data and commands are passed between scripts.

b. Design Central Controller: Design a central controller script that will manage the flow of data and commands between scripts. This script should be designed to handle any issues identified in the bottleneck analysis.

c. Implementation: Rewrite the existing scripts as needed to interact with the central controller, rather than interacting directly with each other. Ensure that the central controller has the necessary functions to manage all required interactions.

d. Testing: Run tests to confirm that the central controller is correctly managing script interactions and that the system is running more efficiently.

### Leveraging Efficient Computing Resources:

a. Identify Resource Intensive Tasks: Identify which parts of the application are most resource-intensive. This could be done by monitoring resource usage during typical tasks.

b. Optimize Libraries and Platforms: Review the libraries and platforms used by the application to identify any that could be replaced with more efficient alternatives. For instance, if the application is currently running on a local machine, consider migrating it to a cloud-based solution that can provide more computing power and scalability.

c. Implement Changes: Replace the identified libraries or platforms with the more efficient alternatives. This may involve rewriting parts of the application to work with the new resources.

d. Testing: Run tests to confirm that the application is running more efficiently and that the changes have not introduced any new issues.

## Modules Currently Used in [SoundSage](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage) and [AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain)

- `tkinter`: Used for creating the GUI.
- `PIL`: Used for image processing.
- `audio_analysis`: Custom module for analyzing audio files.
- `audio_processor`: Custom module for processing audio files.
- `ffprobe`: Used for extracting audio file information.
- `ffmpy`: Used for applying gain adjustment to audio files.
- `shutil`: Used for copying files.
- `openai_interaction`: Custom module for interacting with the OpenAI API.

## Functions

- `open_files()`: Opens the file dialog to select audio files.
- `choose_output_directory()`: Opens the directory dialog to select the output directory.
- `begin_process()`: Starts the audio processing.

## APIs

- [OpenAI API](https://openai.com/policies/terms-of-use): Used for generating Python code based on user input.

## Sources

- [AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain) scripts: `main.py`, `audio_analysis.py`, `audio_processor.py`

## Potential Modules

Here are some potential modules that could be used in the [SoundSage](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage) LLM integration:

- `transformers`: A Python library for state-of-the-art natural language processing, developed by [Hugging Face](https://huggingface.co/terms-of-service). It provides pre-trained models for several major LLMs, including [OpenAI](https://openai.com/policies/terms-of-use)'s GPT-3 and [Google's BERT](https://cloud.google.com/ai-platform/training/docs/algorithms/bert-start). The library is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

- `scikit-learn`: This is a machine learning library in Python. It features various classification, regression and clustering algorithms, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy. This module is distributed under the [3-Clause BSD license​](https://github.com/scikit-learn/scikit-learn).

- `SoundFile`: This Python package can read and write sound files. File reading/writing is supported for many formats including WAV, FLAC, OGG, and more. This module is licensed under the [BSD 3-Clause License​](https://snyk.io/advisor/python/soundfile)​.

- `spaCy`: A Python library for advanced natural language processing. It provides functionalities for part-of-speech tagging, named entity recognition, and dependency parsing, among others. This could be used to enhance the LLM's ability to interpret user prompts. The library is released under the [MIT License](https://opensource.org/licenses/MIT).

- `nltk (Natural Language Toolkit)`: A Python library for working with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources. This could be used to enhance the LLM's understanding of natural language. The library is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

- `torchaudio`: An audio library for PyTorch. It provides a variety of audio transforms, supports audio I/O, and has dataloaders for common audio datasets. This could be used for loading and saving audio files, as well as performing common audio transformations. The library is released under the [BSD-3-Clause](https://github.com/pytorch/audio)

## Licenses

The licensing information for the modules and functions used in the AutoGain scripts is as follows:

- `tkinter`, `PIL`, `shutil`: These are part of the Python Standard Library and are covered by the [Python Software Foundation License](https://docs.python.org/3/license.html).
- `ffprobe`, `ffmpy`: These are licensed under the [GNU General Public License (GPL) version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).
- [AutoGain](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/tree/SoundSage---LLM-Integration/SoundSage-LLM%20Integration/SoundSage/WorkBench/AudioTools/AutoGain) scripts: `main.py`, `audio_analysis.py`, `audio_processor.py`: These are custom modules made by [SoundSage](https://github.com/Gabeiscool420/SoundSage---LLM-Audio-Processing/edit/SoundSage---LLM-Integration) and adhere the to [SoundSage open source license](LICENCE.me).
- [OpenAI API](https://openai.com/policies/terms-of-use): this is part of OpenAI's  [open source license](https://github.com/openai/openai-openapi/blob/master/LICENSE).


   <div style="text-align: center;">
    <img
      src="SoundSage-LLM Integration/LOGO.png"
      alt="Alt text"
      title="Optional title"
      style="display: block; margin: 0 auto; max-width: 30px; width: 10%;">
   </div>


