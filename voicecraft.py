import pyttsx3
import tkinter as tk
from tkinter import ttk

# Initialize the text-to-speech engine
text_to_speech = pyttsx3.init()

# Set properties (optional)
text_to_speech.setProperty("volume", 0.9)  # Volume (0.0 to 1.0)
text_to_speech.setProperty("rate", 150)    # Speed (words per minute)

def convert_to_speech():
    text = input_text.get("1.0", tk.END).strip()
    if text:
        text_to_speech.say(text)
        text_to_speech.runAndWait()

def on_exit():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("400x200")
root.configure(bg="#baffea")  # Set the background color

# Create the text input field
input_text = tk.Text(root, wrap=tk.WORD, font=("Arial", 12, "bold"), height=5)  # Make the text bold
input_text.pack(pady=10, padx=10)

# Create the "Speak" button with custom style
style = ttk.Style()
style.configure("Bold.TButton", font=("Arial", 12, "bold"), foreground="#000000", background="#8b8788")
speak_button = ttk.Button(root, text="Speak", command=convert_to_speech, style="Bold.TButton")
speak_button.pack(pady=5)

# Create the "Exit" button with custom style
exit_button = ttk.Button(root, text="Exit", command=on_exit, style="Bold.TButton")
exit_button.pack(pady=5)

root.mainloop()
