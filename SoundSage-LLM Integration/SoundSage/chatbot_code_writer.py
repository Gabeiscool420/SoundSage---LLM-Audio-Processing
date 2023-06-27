import openai_interaction

def write_code(user_input):
    # Send the user's input to the OpenAI API
    response = openai_interaction.send_input_to_openai(user_input)

    # Extract key information from the response
    processing_type = openai_interaction.extract_info_from_response(response, 'processing_type', default='default_processing_type')
    folder_name = openai_interaction.extract_info_from_response(response, 'folder_name', default='default_folder_name')
    file_selection = openai_interaction.extract_info_from_response(response, 'file_selection', default='all')
    file_type = openai_interaction.extract_info_from_response(response, 'file_type', default='default_file_type')
    directory_name = openai_interaction.extract_info_from_response(response, 'directory_name', default='default_directory_name')
    project_type = openai_interaction.extract_info_from_response(response, 'project_type', default='default_project_type')

    # Confirm or clarify information if necessary
    if processing_type == 'default_processing_type':
        processing_type = openai_interaction.confirm_info('processing_type', processing_type)
    if folder_name == 'default_folder_name':
        folder_name = openai_interaction.confirm_info('folder_name', folder_name)
    # ... repeat for other parameters ...

    # Write the response from the API to a Python file
    with open("generated_code.py", "w") as file:
        file.write(response)

    # Return a message indicating that the code has been written
    return "Code written to generated_code.py."
