import openai_interaction

def write_code(user_input):
    # Send the user's input to the OpenAI API
    response = openai_interaction.send_input_to_openai(user_input)

    # Write the response from the API to a Python file
    with open("generated_code.py", "w") as file:
        file.write(response)

    # Return a message indicating that the code has been written
    return "Code written to generated_code.py."
