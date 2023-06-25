import os

def template_code(directory_path):
    # Navigate to the specified directory
    os.chdir(directory_path)

    # Perform some operation on the files in the directory
    for filename in os.listdir(directory_path):
        print(f"Processing file: {filename}")

    # Return a message indicating that the operation is complete
    return "Operation complete."
