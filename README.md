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

  ## Install these dependencies using pip:
  
  `pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes`

## How to Use

1. Run the Script :

- Ensure your microphone is connected and working.
- Run the script using Python:

python your_script_name.py

2. Command Examples :

- To play a song: "Alexa, play Despacito"
- To get the current time: "Alexa, what is the time?"
- To search Wikipedia: "Alexa, who the heck is Albert Einstein?"
- Ask a joke: "Alexa, tell me a joke"

3. Functionality :
- Playing Songs: Uses pywhatkit to play songs on YouTube.
- Current Time: Retrieves and announces the current time using datetime.
- Wikipedia Search: Provides a summary of a person's information using wikipedia.
- Jokes: Tells a random joke using pyjokes.
- Responses: Includes humorous responses to questions about dating and relationship status.

4. Notes :
- If encountering issues with speech recognition, ensure your microphone is properly configured and accessible.
- Modify the voice settings or behavior as needed in the script.

## Author
`Himani Gohil`
GitHub: 'https://github.com/Himani0002/Himani0002.git'







