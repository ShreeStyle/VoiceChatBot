import json
import random
import pyttsx3  # For text-to-speech
import speech_recognition as sr  # For speech-to-text

# Load the chat data
def load_chat_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Find a response for user input
def get_response(user_input, chat_data):
    # Look for an exact match first
    for chat in chat_data:
        if user_input.lower() == chat["input"].lower():
            return chat["response"]
    # If no match found, give a default response
    return random.choice([
        "Mujhe samajh nahi aaya, beta.",
        "Beta, main thoda busy hoon abhi.",
        "Pyar se baat karte hain, bolo kya baat hai?"
    ])

# Speak the response using text-to-speech
def speak_response(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

# Listen for voice input
def listen_for_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your message...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the speech service.")
            return None

# Main function to run the assistant
def run_virtual_assistant():
    print("Virtual Assistant (Type 'exit' to quit or say 'exit' to quit)")
    chat_data = load_chat_data("chat_data.json")
    
    while True:
        # Listen for voice input
        user_input = listen_for_input()

        if user_input is None:
            continue

        if "exit" in user_input.lower():
            print("Goodbye!")
            speak_response("Goodbye!")
            break
        
        response = get_response(user_input, chat_data)
        print(f"Papa: {response}")
        speak_response(response)

# Run the assistant
if __name__ == "__main__":
    run_virtual_assistant()
