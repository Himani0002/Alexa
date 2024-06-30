
import speech_recognition as sr
import pyttsx3  # Python-text-speech3
import pywhatkit # for song
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer() # machine's ability to listen to spoken words and identify them
engine = pyttsx3.init() # Text-speech variable

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # female voice [1]

def talk(text):

    engine.say(text) # Say --> Text speech
    engine.runAndWait()

def take_command():

        try:
            with sr.Microphone() as source:
                print('Listening...')
                voice = listener.listen(source) # say somthing listener(Alexa)
                command = listener.recognize_google(voice) # Google api and Google will give you a text
                command=command.lower() # uppercase character to lowercase

                if 'alexa' in command: # Only using alexa name to call it
                    command = command.replace('alexa','') # Replace Alexa string to null string
                    print(command) # Functions calling and text-to-speech

        except:
            pass # pass is a null operation — when it is executed, nothing happens.
        return command

def run_alexa():
    command = take_command() # calling
    print(command)

    if 'play' in command:
        song = command.replace('play','')

        talk('playing' + song)
        pywhatkit.playonyt(song) # Playing YouTube giving command

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is'+time)

    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_alexa()


