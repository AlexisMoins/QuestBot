# bot.py
import discord
from source.utils import Utils
from source.players import Players

class QuestBot(discord.Client):

    def __init__(self, server, *args, **kwargs):
        # Initialize discord.Client() with
        # the arguments given to QuestBot()
        super().__init__(*args, **kwargs)

        self.SERVER = server
        self.players = Players.get_array()
        self.reactions = Utils.import_data_from("resources/reactions.yaml")

    async def on_ready(self):
        # Get the server informations
        server = discord.utils.get(self.guilds, name=self.SERVER)

        # Print the bot (name) and the server (name, ID)
        print(f"{self.user.name} est connecté au serveur suivant :\n"
            f"{server.name} (ID : {server.id})")

        # Print the current members of the server
        print(f"\nMembres du serveur :")
        for member in server.members:
            print(f" - {member.name}")

    # Performs certain actions depending on the command typed by the discord user.
    async def on_message(self, message: discord.Message):
        # prevent the bot from replying to its own messages
        if message.author == self.user:
            return

        if message.content.startswith("!info"):
            # The discord user is not yet a player
            await message.channel.send(f"{message.author.mention} Vous n'êtes pas encore un joueur. Utilisez la commande `!nouveau` pour créer un personnage.")

        if message.content.startswith("!nouveau"):
            embed = discord.Embed(title="Séléction de la classe :", description="Les classes suivantes sont disponibles dans le jeu. Réagissez avec l'emoji correspondant pour que cette dernière vous soit attribuée.", color=0xff9300)
            embed.add_field(name="1. Barbare", value="spécialisé dans la force", inline=False)
            embed.add_field(name="2. Magicien", value="spécialisé dans l'intelligence", inline=False)
            embed.add_field(name="3. Archer", value="spécialisé dans la dexterité", inline=False)

            # Get the message sent by the bot
            bot_message = await message.channel.send(embed=embed)
            # Add reactions to the bot's message
            for index in range(3):
                await bot_message.add_reaction(self.reactions["selectors"][index])


    # Get the reaction to a message and its author
    async def on_raw_reaction_add(self, reaction: discord.Reaction):
        # Check wether the message the user is reacting to is the good one
        if reaction.message_id != self.reaction_message_id:
            return
