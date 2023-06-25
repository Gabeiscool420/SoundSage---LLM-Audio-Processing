import openai_interaction

def send_button_click(event, input_field, chat_window):
    # Get the user's input
    user_input = input_field.get("1.0", 'end-1c')

    # Send the user's input to the OpenAI API
    response = openai_interaction.send_input_to_openai(user_input)

    # Display the response in the chat window
    chat_window.insert('end', '\n' + 'ChatBot: ' + response)