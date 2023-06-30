from tkinter import messagebox, Menu, Tk, Text, Button, Scrollbar
import openai_interaction
import menu_functions
import send_button_functionality
import chatbot_code_writer
import error_handling

def main():
    # Initialize the application
    root = Tk()
    root.title("Chat Bot")
    root.geometry("400x500")
    root.resizable(width=False, height=False)

    # Create the main menu
    main_menu = Menu(root)
    root.config(menu=main_menu)

    # Add the file menu to the main menu
    file_menu = Menu(root)
    main_menu.add_cascade(label="File", menu=file_menu)

    # Add commands to the file menu
    file_menu.add_command(label="New..", command=menu_functions.new_file)
    file_menu.add_command(label="Save As..", command=menu_functions.save_as)
    file_menu.add_command(label="Exit", command=root.quit)

    # Add the rest of the menu options to the main menu
    main_menu.add_command(label="Edit", command=menu_functions.edit)
    main_menu.add_command(label="Quit", command=root.quit)

    # Create the chat window
    chatWindow = Text(root, bd=1, bg="black",  width="50", height="8", font=("Arial", 23), foreground="#00ffff")
    chatWindow.place(x=6,y=6, height=385, width=370)

    # Create the message window
    messageWindow = Text(root, bd=0, bg="black",width="30", height="4", font=("Arial", 23), foreground="#00ffff")
    messageWindow.place(x=128, y=400, height=88, width=260)

    # Create the scrollbar
    scrollbar = Scrollbar(root, command=chatWindow.yview, cursor="star")
    scrollbar.place(x=375,y=5, height=385)

    # Create the send button
    sendButton = Button(root, text="Send",  width="12", height=5,
                    bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12),
                    command=lambda: send_button_functionality.send_button_click(None, messageWindow, chatWindow))
    sendButton.place(x=6, y=400, height=88)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        error_handling.handle_error(e)

