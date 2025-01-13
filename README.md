# Voice ChatBot Assistant

This is a simple voice-based chatbot built in Python that allows users to interact with it using speech-to-text and receive responses through text-to-speech.
The chatbot can listen to the user’s voice, recognize it, and reply with a pre-defined response.
It uses the `speech_recognition` library for voice input and the `pyttsx3` library for text-to-speech output.

## Features
- **Voice Input**: Users can talk to the chatbot using speech.
- **Speech-to-Text**: The speech is converted into text for processing.
- **Predefined Responses**: The chatbot will respond with predefined answers based on the input.
- **Text-to-Speech**: The chatbot’s response is spoken out loud.
- **Exit Command**: The chatbot can be exited either by typing "exit" or saying "exit."

## Requirements
Before running the chatbot, you need to install the following libraries:

- `pyttsx3` - for text-to-speech functionality
- `speech_recognition` - for speech-to-text functionality
- `random` and `json` (built-in Python libraries)

You can install the required libraries using the following commands:

```bash
pip install pyttsx3
pip install SpeechRecognition
