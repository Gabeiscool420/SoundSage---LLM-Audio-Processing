1. **User Prompt**
    - Function: `get_user_prompt()`
        - Input: None
        - Output: User's text prompt
    |
    V
2. **LLM Interpretation (openai_interaction.py)**
    - Function: `interpret_prompt(prompt)`
        - Input: User's text prompt
        - Output: Interpreted user intent and relevant information
    - Helper Functions:
        - `extract_keywords(prompt)`: Extracts keywords from the user's prompt
        - `identify_intent(keywords)`: Identifies the user's intent based on the keywords
    |
    V
3. **Command Generation**
    - Function: `generate_commands(interpreted_prompt)`
        - Input: Interpreted user intent and relevant information
        - Output: List of commands for audio processing tools
    - Helper Functions:
        - `map_intent_to_commands(intent)`: Maps the user's intent to the corresponding commands
        - `format_commands(commands)`: Formats the commands in a way that the audio processing tools can understand
    |
    V
4. **Command Execution (file_management.py, autogain_interaction.py)**
    - Function: `execute_commands(commands)`
        - Input: List of commands for audio processing tools
        - Output: Status of command execution (success or failure), processed audio files
    - Helper Functions:
        - `load_audio_files(file_paths)`: Loads the audio files that need to be processed
        - `apply_audio_processing_tasks(commands, audio_files)`: Applies the audio processing tasks to the audio files
        - `save_processed_files(processed_files, destination_folder)`: Saves the processed audio files to the specified location
    |
    V
5. **Error Handling (error_handling.py)**
    - Function: `handle_errors(status)`
        - Input: Status of command execution
        - Output: Error message (if any)
    - Helper Functions:
        - `log_error(error)`: Logs the error for debugging purposes
        - `format_error_message(error)`: Formats the error message in a user-friendly way
    |
    V
6. **Process Completion (completion_handling.py)**
    - Function: `handle_completion(status)`
        - Input: Status of command execution
        - Output: Completion message
    - Helper Functions:
        - `check_process_status(status)`: Checks the status of the process
        - `format_completion_message(status)`: Formats the completion message based on the status of the process
    |
    V
7. **Feedback to User**
    - Function: `generate_feedback(completion_message, error_message)`
        - Input: Completion message, error message (if any)
        - Output: User-friendly feedback message
    - Helper Functions:
        - `combine_messages(completion_message, error_message)`: Combines the completion message and the error message (if any) into a single feedback message
        - `format_feedback_message(feedback_message)`: Formats the feedback message in a user-friendly way
