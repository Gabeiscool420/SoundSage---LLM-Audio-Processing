# SoundSage---LLM-Audio-Processing-Integration
**TODO:*

- [ ] = exists but is not complete
- [x] = is complete

- [>] = Directory(stacks like: >> or >>> etc... for directory within a directory)


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


<div style="text-align: center;">
    <img
      src="SoundSage-LLM Integration/LOGO.png"
      alt="SoundSage Logo"
      title="SoundSage Logo"
      style="display: block; margin: 0 auto; max-width: 30px; width: 10%;">
</div>
