import os
import shutil

def navigate_to_folder(folder_path):
    # Navigate to a specified folder
    os.chdir(folder_path)

def copy_file(source_path, destination_path):
    # Copy a file from source_path to destination_path
    shutil.copy2(source_path, destination_path)

def paste_file(file_path, destination_path):
    # Paste a file at destination_path
    shutil.copy2(file_path, destination_path)
