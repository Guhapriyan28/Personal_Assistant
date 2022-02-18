import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Start Speaking!!")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
except:
    pass



