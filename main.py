# Quest Bot
import discord

from os import getenv, system
from dotenv import load_dotenv
from source.questbot import QuestBot


load_dotenv()
# Get discord variables from .env file
TOKEN = getenv("DISCORD_TOKEN")
SERVER = getenv("DISCORD_SERVER")

system("clear")
intents = discord.Intents.default()
intents.members = True

client = QuestBot(server=SERVER, intents=intents)
client.run(TOKEN)
