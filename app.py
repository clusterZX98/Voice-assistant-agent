
# ===================== CONFIG =====================
ASSISTANT_NAME = "Hector"

# ==================================================

import pyttsx3
import speech_recognition as sr
import datetime
import requests
from bs4 import BeautifulSoup
import webbrowser
import os
import random
import time
import psutil
import pyautogui
import pyperclip
import wikipedia
import subprocess

# --------------------------- SPEAK ---------------------------
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 175)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.1)

# --------------------------- WISH ---------------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(f"Hello sir, I am {ASSISTANT_NAME}. How may I help you?")

# --------------------------- TAKE COMMAND ---------------------------
def takeCommand():
    r = sr.Recognizer()
    r.pause_threshold = 0.6
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        return query.lower()
    except:
        return "none"

# --------------------------- SYSTEM INFO ---------------------------
def system_info():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    speak(f"CPU usage is {cpu} percent")
    speak(f"RAM usage is {ram} percent")

# --------------------------- SCREENSHOT ---------------------------
def take_screenshot():
    file_name = f"screenshot_{int(time.time())}.png"
    pyautogui.screenshot(file_name)
    speak("Screenshot taken")

# --------------------------- TIMER ---------------------------
def set_timer(seconds):
    speak(f"Timer set for {seconds} seconds")
    time.sleep(seconds)
    speak("Time is up")

# --------------------------- AI RESPONSE (FREE) ---------------------------
def ai_chat(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except:
        return "I couldn't find anything on that."

# --------------------------- MAIN ---------------------------
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if query == "none":
            continue

        # EXIT
        elif 'exit' in query or 'bye' in query:
            speak("Goodbye sir")
            break

        # TIME
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        # OPEN WEBSITES
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")
        elif 'open stack overflow' in query:
            speak("Opening Stack Overflow.")
            webbrowser.open("https://stackoverflow.com")

        elif 'open github' in query:
            speak("Opening GitHub.")
            webbrowser.open("https://github.com")

        elif 'open whatsapp' in query:
            speak("Opening WhatsApp Web.")
            webbrowser.open("https://web.whatsapp.com")

        elif 'open facebook' in query:
            speak("Opening Facebook.")
            webbrowser.open("https://facebook.com")

        elif 'open instagram' in query:
            speak("Opening Instagram.")
            webbrowser.open("https://instagram.com")

        # Time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"sir, the time is {strTime}")

        # Open VS Code
        elif 'open code' in query:
            codePath = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio Code.")
            os.startfile(codePath)

        # Jokes, facts, quotes, music
        elif 'joke' in query:
            joke = random.choice(jokes)
            speak(joke)
            print(joke)

        
        # Fun actions
        elif 'flip a coin' in query:
            result = random.choice(['Heads', 'Tails'])
            speak(f"It's {result}!")
            print(f"Coin flip: {result}")

        elif 'roll a dice' in query or 'roll a die' in query:
            dice = random.randint(1, 6)
            speak(f"You rolled a {dice}!")
            print(f"Dice roll: {dice}")

        # SYSTEM INFO
        elif 'system info' in query:
            system_info()

        # SCREENSHOT
        elif 'screenshot' in query:
            take_screenshot()

        # SHUTDOWN
        elif 'shutdown' in query:
            speak("Shutting down")
            os.system("shutdown /s /t 5")

        # RESTART
        elif 'restart' in query:
            speak("Restarting")
            os.system("shutdown /r /t 5")

        # LOCK
        elif 'lock' in query:
            speak("Locking system")
            os.system("rundll32.exe user32.dll,LockWorkStation")

        # VOLUME
        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")

        # CLIPBOARD
        elif 'read clipboard' in query:
            text = pyperclip.paste()
            speak(text)

        # CREATE FOLDER
        elif 'create folder' in query:
            folder = query.replace("create folder", "").strip()
            os.makedirs(folder, exist_ok=True)
            speak("Folder created")

        # OPEN FILE
        elif 'open file' in query:
            file = query.replace("open file", "").strip()
            os.startfile(file)

        # TIMER
        elif 'set timer' in query:
            try:
                seconds = int(query.split()[-1])
                set_timer(seconds)
            except:
                speak("Please specify seconds")

        # JOKE
        elif 'joke' in query:
            jokes = [
                "Why don't programmers like nature? Too many bugs.",
                "Why did Python go to school? To become smarter."
            ]
            speak(random.choice(jokes))

        # SEARCH
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        # AI CHAT
        else:
            response = ai_chat(query)
            speak(response)
            print(response)