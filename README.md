Sure! Here's a README file for your voice assistant project using Python:

---

# 🎙️ Alexa Voice Assistant Clone

Welcome to the Alexa Voice Assistant Clone project! This project is a simplified version of a voice assistant that can perform various tasks such as playing music, telling the time, providing Wikipedia summaries, and telling jokes. Enjoy exploring and customizing it! 🌟

## 📦 Features

- **Play Music** 🎵
- **Tell the Time** 🕒
- **Provide Wikipedia Summaries** 📚
- **Tell Jokes** 😂
- **Engage in Fun Conversations** 💬

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Required Python packages: `speech_recognition`, `pyttsx3`, `pywhatkit`, `datetime`, `wikipedia`, `pyjokes`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/alexa-clone.git
   cd alexa-clone
   ```

2. **Install the required packages:**
   ```bash
   pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes
   ```

3. **Run the project:**
   ```bash
   python main.py
   ```

## 🛠️ Technologies Used

- **Python** - The programming language used
- **speech_recognition** - For recognizing voice commands
- **pyttsx3** - For text-to-speech conversion
- **pywhatkit** - For playing music on YouTube
- **wikipedia** - For fetching summaries from Wikipedia
- **pyjokes** - For telling jokes

## 📜 Code Overview

```python
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
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

while True:
    run_alexa()
```

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📧 Contact

If you have any questions or suggestions, feel free to reach out:

- **Email:** himanigohil@0002gmail.com
- **GitHub:** [himani0002](https://github.com/himani0002)
- **Web:** [Project Link](https://66a77680ee416621d0c6e2cf--lambent-cheesecake-d35721.netlify.app/)

---

Happy coding! 💻✨

---

Feel free to customize this README further if needed!
