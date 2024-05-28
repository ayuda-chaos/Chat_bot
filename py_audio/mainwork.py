import pyttsx3 as p
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import os

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, duration=0.5)  # Shorten duration to 0.5 seconds
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print("Sorry, there was an error with the request: {0}".format(e))
            return ""

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant created by Aayush. How are you?")

def search_wikipedia(query):
    speak("Searching Wikipedia...")
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia, " + result)
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any information on that.")
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple matches for that query. Can you please be more specific?")

def open_youtube():
    url = "https://www.youtube.com/"
    speak("Opening YouTube")
    webbrowser.open(url)

def open_website(url):
    speak("Opening ")
    webbrowser.open(url)

def open_application(app_name):
    app_path = {
        "notepad": "C:\\Windows\\System32\\notepad.exe",
        "calculator": "C:\\Windows\\System32\\calc.exe",
        "paint": "C:\\Windows\\System32\\mspaint.exe"
        
    }

def main():
    wish_me()
    while True:
        text = listen()
        if "what about you" in text:
            speak("I'm having a good day. How may i assist you.")
        elif "Who Help me to learn Python" in text:  
            speak("My professor Jim Scripture")
        elif "what can you do" in text:
            speak("I can assist you with various tasks such as checking the weather, searching the web, setting reminders, and more. Just let me know what you need")
        elif "search wikipedia for" in text:
            query = text.replace("search wikipedia for", "").strip()
            search_wikipedia(query)
        elif "open my website" in text:  
            open_website("https://aayushtimalsina.com.np/")
        elif "open website" in text:
            url = text.replace("open website", "").strip()
            open_website(url)
        elif "open youtube" in text:  
            open_youtube()
        elif "open" in text:
            app_name = text.replace("open", "").strip()
            open_application(app_name)
        elif "thank you" in text:
            speak("You're welcome!")
        elif "goodbye" in text or "bye" in text:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm sorry, I didn't catch that. Could you please repeat?")
            continue

if __name__ == "__main__":
    main()