import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import subprocess
import webbrowser

# Initialize recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def talk(text):
    print(f"My assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        talk("Good morning, HARITHA!")
    elif 12 <= hour < 18:
        talk("Good afternoon, HARITHA!")
    else:
        talk("Good evening, HARITHA!")
    talk("How can I assist you today?")

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source, phrase_time_limit=6)
            command = listener.recognize_google(audio)
            command = command.lower()
            print(f"You said: {command}")
            return command
    except:
        return ""

def open_downloads_folder():
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    if os.path.exists(downloads_path):
        talk("Opening Downloads folder")
        os.startfile(downloads_path)
    else:
        talk("Downloads folder not found.")

def open_vscode():
    vscode_folder = r"C:\Users\chshe31\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
    if os.path.exists(vscode_folder):
        for item in os.listdir(vscode_folder):
            if item.lower().endswith(".lnk"):  # Look for shortcut
                vscode_shortcut = os.path.join(vscode_folder, item)
                talk("Opening Visual Studio Code")
                os.startfile(vscode_shortcut)
                return
        talk("VS Code shortcut not found in the folder.")
    else:
        talk("VS Code folder not found.")

def run_assistant():
    wish_user()

    while True:
        command = take_command()

        if not command:
            continue

        if 'stop' in command or 'exit' in command:
            talk("Thank you Hari, have a great day! Goodbye!")
            break

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The current time is {time}")

        elif 'play' in command and 'youtube' in command:
            song = command.replace('play', '').replace('on youtube', '').strip()
            talk(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif 'open notepad' in command:
            talk("Opening Notepad")
            os.system("notepad.exe")

        elif 'open mysql' in command:
            mysql_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL"
            if os.path.exists(mysql_path):
                os.startfile(mysql_path)
                talk("Opening MySQL Workbench")
            else:
                talk("MySQL Workbench shortcut not found")

        elif 'open youtube' in command:
            talk("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open chrome' in command or 'search' in command:
            if 'search' in command:
                query = command.replace('search', '').replace('open chrome', '').strip()
                talk(f"Searching for {query} on Chrome")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                talk("Opening Chrome")
                webbrowser.open("https://www.google.com")

        elif 'open downloads' in command:
            open_downloads_folder()

        elif 'open vs code' in command or 'start vs code' in command:
            open_vscode()

        else:
            talk("Sorry, I didn't understand that. Please try again.")

# Run the assistant
run_assistant()
