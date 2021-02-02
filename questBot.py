# Quest Bot
import os
import discord

from src.bot import QuestBot
from dotenv import load_dotenv


load_dotenv()
# Get discord variables from .env file
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")


client = QuestBot(server=SERVER)
client.run(TOKEN)
