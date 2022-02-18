import speech_recognition as sr
import pyttsx3
import pywhatkit as pwt
import wikipedia
import datetime
import pyjokes
import sys

listener = sr.Recognizer()
global command

def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


def main_fuc():
    try:
        with sr.Microphone() as source:
            print("I am listening...")
            speak('I am listening...')

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'victor' in command:
                command = command.replace('victor', '')
            print(command)

    except:
        pass

    return command

def start_victor():
    command = main_fuc()
    # song request -----------------------------------------------------------------------------------------
    if 'play' in command:
        song = command.replace('play', '')
        print(song)
        speak('playing the song')
        pwt.playonyt(song)
        sys.exit()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        speak('Time is '+time)
        print(time)
    elif 'who is ' in command:
        person = command.replace('who is ', '')
        info_person = wikipedia.summary(person, 1)
        print(info_person)
        speak(info_person)
    elif 'are you single' in command:
        speak('NO I am in relationship  with wifi')
        print('NO I am in relationship  with wifi')
    elif 'what is ' in command:
        info_con = command
        pwt.search(info_con)
        speak('Let me show you the details')
        sys.exit()

    elif 'stop' in command:
        sys.exit()
    elif 'joke' in command:
        speak(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        speak('I could not hear you properly')

while True:
    start_victor()


