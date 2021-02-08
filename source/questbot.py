# questbot.py
import discord
from .utils import Utils
from .player import Player

class QuestBot(discord.Client):

    # The ID of the class selection message
    class_selection_message_id = 0

    def __init__(self, server, *args, **kwargs):
        # Initialize discord.Client() with
        # the arguments given to QuestBot()
        super().__init__(*args, **kwargs)

        self.server_name = server
        self.players = Player.build_array()

    # Perforns certain actions when the bot is connected and running
    async def on_ready(self):
        # Get the server informations
        self.server = discord.utils.get(self.guilds, name=self.server_name)

        # Print the bot (name) and the server (name, ID)
        print(f"\n{self.user.name} is connected to server :\n"
            f"{self.server.name} -> {self.server.id}\n")

        # Print the current members (name, ID) of the server
        print(f"Server members :")
        for member in self.server.members:
            # Don't print bots informations
            if not member.bot :
                print(f" - {member.name} -> {member.id}")

    async def on_disconnect(self):
        print("\nQuestBot disconnected from server")
        for key, value in self.players.items():
            value.serialize()

    # Performs certain actions depending on the command typed by the discord user
    async def on_message(self, message: discord.Message):
        # prevent the bot from replying to its own messages
        if message.author == self.user:
            return

        if message.content.startswith("!bye") and message.author.id == 144436069264261120:
            await self.close()

        if message.content.startswith("!info"):
            # Check wether the player already exists
            if not Utils.player_exists(message.author.id):
                # The discord user is not yet a player
                await message.channel.send(f"{message.author.mention} Vous n'êtes pas encore un joueur. Utilisez la commande `!nouveau` pour créer un personnage.")
            else:
                # Building my own embed message
                embed = self.players[str(message.author.id)].informations(message.author)
                # Get the message sent by the bot
                bot_message = await message.channel.send(embed=embed)

        if message.content.startswith("!nouveau"):
            # Check wether the user is already a player
            if Utils.player_exists(message.author.id):
                await message.channel.send(f"{message.author.mention} Vous faite déjà parti des joueurs")
                return

            # Building my own embed message
            embed = Utils.build_message("nouveau")
            # Get the message sent by the bot
            bot_message = await message.channel.send(embed=embed)
            # Add reactions to the bot's message
            await bot_message.add_reaction("1️⃣")
            await bot_message.add_reaction("2️⃣")
            await bot_message.add_reaction("3️⃣")

            # Change the reaction message ID saved in Classes.py
            self.class_selection_message_id = bot_message.id

    # Get the reaction to a message and its author
    async def on_raw_reaction_add(self, reaction: discord.RawReactionActionEvent):
        # Ensure the bot's reactions are not taken into account
        if reaction.user_id == self.user.id:
            return

        # Check wether the user is already a player
        if reaction.user_id not in self.players:
            # Ensure the message being reacted to is the one for class selection
            if reaction.message_id == self.class_selection_message_id:

                if reaction.emoji.name == "1️⃣":
                    player_class = "barbarian"
                    role_ID = 806577781722710097
                elif reaction.emoji.name == "2️⃣":
                    player_class = "magician"
                    role_ID = 806577926841171989
                elif reaction.emoji.name == "3️⃣":
                    player_class = "archer"
                    role_ID = 806577978863517697

                await self.add_player(reaction, player_class, role_ID)

    # Add a player to the players array
    async def add_player(self, reaction: discord.RawReactionActionEvent, player_class: str, role_ID: int):
        # Empty the message ID variable
        QuestBot.class_selection_message_id = None

        new_player = Player.create_new(reaction.user_id, player_class)
        self.players[reaction.user_id] = new_player

        role = self.server.get_role(role_ID)
        await reaction.member.add_roles(role)
