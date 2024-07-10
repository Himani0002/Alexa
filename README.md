# Alexa-like Voice Assistant

This Python script implements a basic voice assistant similar to Amazon Alexa. It listens for voice commands, processes them, and performs actions such as playing songs on YouTube, telling the current time, providing information from Wikipedia, telling jokes, and responding to specific questions.

## Features

- Play songs on YouTube
- Tell the current time
- Provide summaries from Wikipedia
- Tell jokes
- Respond to specific questions

## Requirements

Ensure you have the following libraries installed before running the script:
- `speech_recognition`
- `pyttsx3`
- `pywhatkit`
- `wikipedia`
- `pyjokes`

You can install these dependencies using pip:

```bash
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes

Usage
Ensure your microphone is connected and working.
Run the script.
Speak commands prefixed with "alexa". For example:
"Alexa, play Despacito"
"Alexa, what is the time?"
"Alexa, who the heck is Albert Einstein?"
"Alexa, tell me a joke"
The voice assistant will respond to these commands accordingly.

Code Explanation
Initializing the Voice Engine

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set to female voice

listener: Recognizer instance to capture and recognize speech.
engine: Text-to-speech engine instance.
voices: List of available voices in the text-to-speech engine.
engine.setProperty('voice', voices[1].id): Sets the voice to female (index 1).

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk(text): Converts the given text to speech and speaks it out.

Listening and Recognizing Command

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

take_command(): Listens to the microphone input, recognizes the speech using Google's speech recognition, converts it to lowercase, and returns the command after removing the keyword "alexa".

Running the Voice Assistant

def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is ' + time)

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

run_alexa(): Executes the appropriate action based on the command recognized.

while True:
    run_alexa()

Continuously runs the run_alexa() function to keep the voice assistant active and listening for commands.

License
This project is licensed under the MIT License.


This `README.md` file provides an overview of the project, installation instructions, usage examples, and a brief explanation of the code.
