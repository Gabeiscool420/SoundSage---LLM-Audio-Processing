import openai_interaction
import tkinter as tk

def send_button_click(event, input_field, chat_window):
    # Get the user's input
    user_input = input_field.get("1.0", 'end-1c')

    # Clear the input field
    input_field.delete("1.0", tk.END)

    try:
        # Send the user's input to the OpenAI API
        response = openai_interaction.send_input_to_openai(user_input)

        # Display the response in the chat window
        chat_window.insert('end', '\n' + 'ChatBot: ' + response)

        # Scroll the chat window to the bottom
        chat_window.see(tk.END)
    except Exception as e:
        # Display the error in the chat window
        chat_window.insert('end', '\n' + 'ChatBot: ' + 'An error occurred: ' + str(e))

        # Scroll the chat window to the bottom
        chat_window.see(tk.END)

