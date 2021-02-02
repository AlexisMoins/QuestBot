# Quest Bot
import os
import yaml

import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(f'{bot.user.name} est connecté au serveur suivant :\n'
        f'{guild.name} (id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'\nMembres du serveur :\n - {members}')


@bot.command(name="bonjour")
async def _bonjour(ctx):
    await ctx.send("Bonjour")

bot.run(TOKEN)
