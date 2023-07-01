import openai_interaction
import tkinter as tk
import file_management

def send_button_click(event, input_field, chat_window):
    # Get the user's input
    user_input = input_field.get("1.0", 'end-1c')

    # Clear the input field
    input_field.delete("1.0", tk.END)

    try:
        # Send the user's input to the OpenAI API
        response = openai_interaction.send_input_to_openai(user_input)
        print(f"Response: {response}")  # Print the response

        # Extract the necessary information from the response
        extracted_info = openai_interaction.extract_info_from_response(response)
        print(f"Extracted info: {extracted_info}")  # Print the extracted information

        # Confirm the extracted information with the user
        for keyword, value in extracted_info.items():
            if value is not None and not openai_interaction.confirm_info(keyword, value):
                # If the user does not confirm the information, display an error message and return
                chat_window.insert('end',
                                   '\n' + 'ChatBot: ' + f'The provided {keyword} is incorrect. Please try again.')
                chat_window.see(tk.END)
                return

        # If all the information is confirmed, find the directory
        directory_paths = file_management.find_directory(extracted_info["directory_name"])

        # Confirm the directory
        confirmed_directory_path = file_management.confirm_directory(directory_paths)

        # If a directory was confirmed, print its path
        if confirmed_directory_path:
            print(f"Confirmed directory: {confirmed_directory_path}")
        else:
            print("No directory was confirmed.")

        # If a directory was confirmed, move the specified files to the PreProcess directory
        if confirmed_directory_path:
            file_management.copy_files_to_preprocess(confirmed_directory_path, extracted_info["file_names"])

        # Display the response in the chat window
        chat_window.insert('end', '\n' + 'ChatBot: ' + response)

        # Scroll the chat window to the bottom
        chat_window.see(tk.END)
    except Exception as e:
        # Display the error in the chat window
        chat_window.insert('end', '\n' + 'ChatBot: ' + 'An error occurred: ' + str(e))

        # Scroll the chat window to the bottom
        chat_window.see(tk.END)
