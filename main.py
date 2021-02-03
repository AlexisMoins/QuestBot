# Quest Bot
import os
import discord

from dotenv import load_dotenv
from source.questbot import QuestBot


load_dotenv()
# Get discord variables from .env file
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")

intents = discord.Intents.default()
intents.members = True

client = QuestBot(server=SERVER, intents=intents)
client.run(TOKEN)
