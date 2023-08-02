# Voice to Text Transcription Application

This is a simple Voice to Text Transcription application written in Python using the Tkinter GUI library for the user interface and the SpeechRecognition library to perform the speech-to-text conversion. The transcribed text can be copied to the clipboard for further use.

## Prerequisites
- Python 3.x installed on your system.
- SpeechRecognition library installed. You can install it using the following command:
  ```
  pip install SpeechRecognition
  ```
- The application requires an internet connection to use the 'recognize_google' method for Google Web Speech API. For offline recognition, you can use 'recognize_sphinx' (CMU Sphinx) or other available engines.

## Usage
1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script (`voice_to_text.py`) is located.

3. Run the application by executing the following command:
   ```
   python voice_to_text.py
   ```

4. The application GUI will appear with a dropdown menu to select the language for transcription.

5. Click the "Start Transcribing" button to begin speech recognition. The application will start listening for your voice input through the microphone.

6. Speak clearly into the microphone, and the application will attempt to transcribe your speech into text. The transcribed text will be displayed in the text box below.

7. If the speech recognition process is successful, the transcribed text will be displayed in the text box. If there are any issues with recognition, appropriate error messages will be displayed.

8. You can select a different language from the dropdown menu if needed.

9. To copy the transcribed text to the clipboard, click the "Copy to Clipboard" button.

10. To transcribe another speech input, simply click the "Start Transcribing" button again.

## Language Options
The application supports multiple languages for speech recognition. By default, the language is set to "English (United States)". You can choose from the following available languages in the dropdown menu:
- English (United States)
- English (United Kingdom)
- Spanish
- French
- German
- Italian
- Japanese

You can also add more languages and their respective language codes to the `languages` dictionary in the script.

## Important Note
- The application uses the 'recognize_google' method by default, which requires an internet connection to access the Google Web Speech API for speech recognition. If you want to use offline recognition, consider using 'recognize_sphinx' or other available engines.

## Disclaimer
**USE AT YOUR OWN RISK. THE DEVELOPER IS NOT RESPONSIBLE FOR ANY UNINTENDED CONSEQUENCES CAUSED BY THE USAGE OF THIS APPLICATION.**

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for any non-malicious purpose.

## Contributions
Contributions to this project are welcome. If you find any issues or want to add enhancements, please submit a pull request.

## Contact
For any questions or inquiries, please contact me
