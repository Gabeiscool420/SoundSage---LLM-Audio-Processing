<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>1. User Prompt</h2>
<p>Function: <code>get_user_prompt()</code><br>
Input: None<br>
Output: User's text prompt</p>
</div>
<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>2. LLM Interpretation (openai_interaction.py)</h2>
<p>Function: <code>interpret_prompt(prompt)</code><br>
Input: User's text prompt<br>
Output: Interpreted user intent and relevant information<br>
Helper Functions:<br>
<code>extract_keywords(prompt)</code>: Extracts keywords from the user's prompt<br>
<code>identify_intent(keywords)</code>: Identifies the user's intent based on the keywords</p>
</div>
<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>3. Command Generation</h2>
<p>Function: <code>generate_commands(interpreted_prompt)</code><br>
Input: Interpreted user intent and relevant information<br>
Output: List of commands for audio processing tools<br>
Helper Functions:<br>
<code>map_intent_to_commands(intent)</code>: Maps the user's intent to the corresponding commands<br>
<code>format_commands(commands)</code>: Formats the commands in a way that the audio processing tools can understand</p>
</div>
<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>4. Command Execution (file_management.py, autogain_interaction.py)</h2>
<p>Function: <code>execute_commands(commands)</code><br>
Input: List of commands for audio processing tools<br>
Output: Status of command execution (success or failure), processed audio files<br>
Helper Functions:<br>
<code>load_audio_files(file_paths)</code>: Loads the audio files that need to be processed<br>
<code>apply_audio_processing_tasks(commands, audio_files)</code>: Applies the audio processing tasks to the audio files<br>
<code>save_processed_files(processed_files, destination_folder)</code>: Saves the processed audio files to the specified location</p>
</div>
<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>5. Error Handling (error_handling.py)</h2>
<p>Function: <code>handle_errors(status)</code><br>
Input: Status of command execution<br>
Output: Error message (if any)<br>
Helper Functions:<br>
<code>log_error(error)</code>: Logs the error for debugging purposes<br>
<code>format_error_message(error)</code>: Formats the error message in a user-friendly way</p>
</div>
<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>6. Process Completion (completion_handling.py)</h2>
<p>Function: <code>handle_completion(status)</code><br>
Input: Status of command execution<br>
Output: Completion message<br>
Helper Functions:<br>
<code>check_process_status(status)</code>: Checks the status of the process<br>
<code>format_completion_message(status)</code>: Formats the completion message based on the status of the process</p>
</div>
<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>7. Feedback to User</h2>
<p>Function: <code>generate_feedback(completion_message, error_message)</code><br>
Input: Completion message, error message (if any)<br>
Output: User-friendly feedback message<br>
Helper Functions:<br>
<code>combine_messages(completion_message, error_message)</code>: Combines the completion message and the error message (if any) into a single feedback message<br>
<code>format_feedback_message(feedback_message)</code>: Formats the feedback message in a user-friendly way</p>
</div>
