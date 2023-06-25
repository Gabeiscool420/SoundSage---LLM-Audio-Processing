import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance
import audio_analysis
import audio_processor


def open_files():
    global audio_files
    audio_files = list(filedialog.askopenfilenames(filetypes=[("Audio files", "*.wav")]))
    file_label.config(text=" ".join(audio_files))

def choose_output_directory():
    global output_directory
    output_directory = filedialog.askdirectory()
    output_label.config(text=output_directory)

def begin_process():
    for audio_file in audio_files:
        analyzed_data = audio_analysis.analyze_audio(audio_file)
        audio_processor.process_audio(audio_file, analyzed_data, output_directory)

root = tk.Tk()
root.title("AutoGain by SoundSage")

# Make the window square and resizable
root.geometry("1200x1200")
root.resizable(True, True)

audio_files = []
output_directory = ""

# Load the logo image
logo_image = Image.open("LOGO.png")

# Resize the logo and set the opacity
logo_width, logo_height = logo_image.size
logo_image = logo_image.resize((int(1.25 * logo_width), int(1.25 * logo_height)), Image.ANTIALIAS)
logo_image = ImageEnhance.Brightness(logo_image).enhance(0.5)

# Create a PhotoImage instance of the logo
logo_photo = ImageTk.PhotoImage(logo_image)

# Add the logo as a background image with the desired background color
logo_label = tk.Label(root, image=logo_photo, bg="#DBC6B1")
logo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set the window color
root.configure(bg="#DBC6B1")

# Create UI elements with custom styling
file_button = tk.Button(root, text="Choose Stems", command=open_files, bg="white", fg="black", font=("Helvetica", 10, "bold"), bd=0, height=2, width=20)
file_button.place(relx=0.1, rely=0.25, anchor=tk.CENTER)

file_label = tk.Label(root, text="", wraplength=400, bg="#F1EAE2", fg="black")
file_label.place(relx=0.038, rely=0.30, anchor=tk.CENTER)

output_button = tk.Button(root, text="Export to...", command=choose_output_directory, bg="white", fg="black", font=("Helvetica", 10, "bold"), bd=0, height=2, width=20)
output_button.place(relx=0.1, rely=0.45, anchor=tk.CENTER)

output_label = tk.Label(root, text="", wraplength=400, bg="#F1EAE2", fg="black")
output_label.place(relx=0.038, rely=0.50, anchor=tk.CENTER)

begin_button = tk.Button(root, text="Begin", command=begin_process, bg="white", fg="black", font=("Helvetica", 14, "bold"), bd=0, height=4, width=23)
begin_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

root.mainloop()
