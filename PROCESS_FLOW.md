<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>1. User Prompt</h2>
<p>Function: <code>get_user_prompt()</code><br>
Input: None<br>
Output: User's text prompt</p>
    
<pre><code class="language-python">
def get_user_prompt():    #TODO: Implement function to get user's text prompt                       
pass     
</code></pre>
</div>

<pre><code class="language-python">
def validate_user_prompt(prompt):    #TODO: Implement function to validate user's text prompt                  
pass
</code></pre>
</div>

<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>2. LLM Interpretation (openai_interaction.py)</h2>
<p>Function: <code>interpret_prompt(prompt)</code><br>
Input: User's text prompt<br>
Output: Interpreted user intent and relevant information<br>
Helper Functions:<br>
<code>extract_keywords(prompt)</code>: Extracts keywords from the user's prompt<br>
<code>identify_intent(keywords)</code>: Identifies the user's intent based on the keywords</p>

<pre><code class="language-python">
def interpret_prompt(prompt):    #TODO: Implement function to interpret user's text prompt                 
pass      
</code></pre>
</div>
                                                                 
<pre><code class="language-python">
def extract_keywords(prompt):    #TODO: Implement function to extract keywords from user's prompt                                                         
pass                                                                       
</code></pre>
</div>

<pre><code class="language-python">
def identify_intent(keywords):    #TODO: Implement function to identify user's intent based on keywords     
pass
</code></pre>
</div>

<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>3. Command Generation</h2>
<p>Function: <code>generate_commands(interpreted_prompt)</code><br>
Input: Interpreted user intent and relevant information<br>
Output: List of commands for audio processing tools<br>
Helper Functions:<br>
<code>map_intent_to_commands(intent)</code>: Maps the user's intent to the corresponding commands<br>
<code>format_commands(commands)</code>: Formats the commands in a way that the audio processing tools can understand</p>

<pre><code class="language-python">
def generate_commands(interpreted_prompt):    #TODO: Implement function to generate commands based on interpreted promp 
pass  
</code></pre>
</div>                                                                     

<pre><code class="language-python">    
def map_intent_to_commands(intent):    #TODO: Implement function to map user's intent to corresponding commands  
pass                                                                       
</code></pre>
</div>

<pre><code class="language-python">
def format_commands(commands):    #TODO: Implement function to format commands for audio processing tools   
pass                                                                       
</code></pre>
</div>

<pre><code class="language-python">
def validate_commands(commands):    #TODO: Implement function to validate commands                            
pass
</code></pre>
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

<pre><code class="language-python">
def execute_commands(commands):   #TODO: Implement function to execute commands                             
pass  
</code></pre>
</div>                                                                     

<pre><code class="language-python">
def load_audio_files(file_paths):    #TODO: Implement function to load audio files                             
pass               
</code></pre>
</div>                                                        

<pre><code class="language-python">
def apply_audio_processing_tasks(commands, audio_files):    #TODO: Implement function to apply audio processing tasks to audio files  
pass    
</code></pre>
</div>                                                                   

<pre><code class="language-python">
def save_processed_files(processed_files, destination_folder):    #TODO: Implement function to save processed audio files                   
pass    
</code></pre>
</div>                                                                   

<pre><code class="language-python">
def track_execution_progress():    #TODO: Implement function to track progress of command execution          
pass
</code></pre>
</div>

<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>5. Error Handling (error_handling.py)</h2>
<p>Function: <code>handle_errors(status)</code><br>
Input: Status of command execution<br>
Output: Error message (if any)<br>
Helper Functions:<br>
<code>log_error(error)</code>: Logs the error for debugging purposes<br>
<code>format_error_message(error)</code>: Formats the error message in a user-friendly way</p>

<pre><code class="language-python">
def handle_errors(status):    #TODO: Implement function to handle errors                                
pass  
</code></pre>
</div>                                                                     

<pre><code class="language-python">
def log_error(error):    #TODO: Implement function to log errors                                   
pass                                                             
</code></pre>
</div>                                                                  

<pre><code class="language-python">
def format_error_message(error):    #TODO: Implement function to format error messages                        
pass   
</code></pre>
</div>                                                                    

<pre><code class="language-python">
def classify_error(error):    #TODO: Implement function to classify errors                              
pass                                                                       
</code></pre>
</div>

<pre><code class="language-python">
def recover_from_error(error):    #TODO: Implement function to recover from errors                          
pass
</code></pre>
</div>

<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>6. Process Completion (completion_handling.py)</h2>
<p>Function: <code>handle_completion(status)</code><br>
Input: Status of command execution<br>
Output: Completion message<br>
Helper Functions:<br>
<code>check_process_status(status)</code>: Checks the status of the process<br>
<code>format_completion_message(status)</code>: Formats the completion message based on the status of the process</p>

<pre><code class="language-python">
def handle_completion(status):    #TODO: Implement function to handle process completion                    
pass   
</code></pre>
</div>
                                                                    
<pre><code class="language-python">
def check_process_status(status):    #TODO: Implement function to check process status                         
pass       
</code></pre>
</div>                                                                

<pre><code class="language-python">
def format_completion_message(status):    #TODO: Implement function to format completion messages                   
pass    
</code></pre>
</div>                                                                   

<pre><code class="language-python">
def cleanup_resources():    #TODO: Implement function to clean up resources used during the process   
pass
</code></pre>
</div>

<div style='background-color: #e0f7fa; padding: 10px; margin-bottom: 10px;'>
<h2>7. Feedback to User</h2>
<p>Function: <code>generate_feedback(completion_message, error_message)</code><br>
Input: Completion message, error message (if any)<br>
Output: User-friendly feedback message<br>
Helper Functions:<br>
<code>combine_messages(completion_message, error_message)</code>: Combines the completion message and the error message (if any) into a single feedback message<br>
<code>format_feedback_message(feedback_message)</code>: Formats the feedback message in a user-friendly way</p>

<pre><code class="language-python">
def generate_feedback(completion_message, error_message):   #TODO: Implement function to generate user feedback                       
pass 
</code></pre>
</div>                                                                      

<pre><code class="language-python">
def combine_messages(completion_message, error_message):    #TODO: Implement function to combine completion and error messages        
pass  
</code></pre>
</div>                                                                     

<pre><code class="language-python">
def format_feedback_message(feedback_message):    #TODO: Implement function to format feedback messages                     
pass     </code></pre>
</div>                                                                  

<pre><code class="language-python">
def handle_different_types_of_feedback(feedback_type):    #TODO: Implement function to handle different types of feedback           
pass
</code></pre>
</div>

