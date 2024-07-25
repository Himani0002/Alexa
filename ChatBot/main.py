import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

TOKEN="https://discord.com/oauth2/authorize?client_id=1265926836924452905&permissions=2199023847552&integration_type=0&scope=bot"
# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Initialize the bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)
print("Client running...")

# Load and train the chatbot model
chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$aibot"):
        user_input = message.content[7:].strip()
        response = chatbot.request(user_input)
        await message.channel.send(response)

client.run(TOKEN)
