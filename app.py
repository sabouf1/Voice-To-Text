import tkinter as tk
import speech_recognition as sr
import pyperclip

def transcribe_audio():
    recognizer = sr.Recognizer()
    language = language_var.get()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio_data = recognizer.listen(source)

    try:
        # Use the 'recognize_google' method for Google Web Speech API (requires an internet connection)
        # For offline recognition, you can use 'recognize_sphinx' (CMU Sphinx)
        # You can also use other engines like 'recognize_bing' for Microsoft Bing Voice Recognition.
        text = recognizer.recognize_google(audio_data, language=language)
        text_entry.delete(1.0, tk.END)  # Clear previous text in the text box
        text_entry.insert(tk.END, text)
    except sr.UnknownValueError:
        text_entry.delete(1.0, tk.END)  # Clear previous text in the text box
        text_entry.insert(tk.END, "Speech recognition could not understand the audio.")
    except sr.RequestError as e:
        text_entry.delete(1.0, tk.END)  # Clear previous text in the text box
        text_entry.insert(tk.END, f"Could not request results from Google Web Speech API; {e}")

def copy_to_clipboard():
    text = text_entry.get(1.0, tk.END).strip()
    if text:
        pyperclip.copy(text)

# Create the GUI
root = tk.Tk()
root.title("Voice to Text Transcription")

# Language options for the dropdown menu
languages = {
    "English (United States)": "en-US",
    "English (United Kingdom)": "en-GB",
    "Spanish": "es-ES",
    "French": "fr-FR",
    "German": "de-DE",
    "Italian": "it-IT",
    "Japanese": "ja-JP",
    # Add more languages and their respective language codes here
}

# Variable to store the selected language
language_var = tk.StringVar(root)
language_var.set("en-US")  # Default language

# Create a dropdown menu for language selection
language_menu = tk.OptionMenu(root, language_var, *languages.keys())
language_menu.pack(pady=5)

# Create a text box to display the transcribed text
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=50)
text_entry.pack(pady=10)

# Create a button to start transcribing
transcribe_button = tk.Button(root, text="Start Transcribing", command=transcribe_audio)
transcribe_button.pack(pady=5)

# Create a button to copy transcribed text to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

root.mainloop()
