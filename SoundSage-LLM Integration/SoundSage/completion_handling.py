import os

def signal_completion_to_llm():
    # Signal to the LLM that the process is complete
    print("Process complete. Signaling to LLM...")

def check_new_folder(new_folder_path):
    # Check the new folder to ensure that the process completed successfully
    if os.path.exists(new_folder_path):
        print("New folder exists. Process completed successfully.")
    else:
        print("New folder does not exist. Process did not complete successfully.")
