import pyttsx3
import datetime
import speech_recognition as sr
import time
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak("Good Morning, I am Jarvis. How can I help you?")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, I am Jarvis. How can I help you?")

    else:
        speak("Good Evening, I am Jarvis. How can I help you?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=5)

    query = r.recognize_google(audio)

    print("User said:", query)

    return query

wishMe()

command = takeCommand().lower()
print(command)

if "time" in command:
    current_time = datetime.datetime.now().strftime("%H:%M")
    print(current_time)

    speak(f"The time is {current_time}")

if "youtube" in command:
    print("Opening youtube")
    speak("Opening youtube")
    webbrowser.open("https://www.youtube.com")

if "google" in command:
    print("Opening google")
    speak("Opening google")
    webbrowser.open("https://www.google.com")

if "notepad" in command:
    print("Opening notepad")
    speak("Opening notepad")
    os.system("notepad")


