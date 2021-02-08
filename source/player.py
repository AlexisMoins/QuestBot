# player.py
import yaml
from .utils import Utils
from discord import Embed
from shutil import copyfile

class Player():

    def __init__(self):
        # The array containing all the messages the player can react to
        self.message_cache = dict()

    @staticmethod
    # Returns an array of Players() built from the data in the resources folder
    def build_array() -> dict:
        players = dict()
        # Get the players' ID from a file
        player_list = Utils.get_player_list()
        print(f"Found {len(player_list)} registered player(s)")

        # Ensure names is a non empty dictionary
        if bool(player_list):
            for player in player_list:
                # Add the discord user ID to the players dict with its
                # corresponding Player instance
                players[player] = Player.deserialize(player)

        return players

    @staticmethod
    # Returns a new Player, constructed from a class file
    def create_new(ID: int, player_class: str):
        # Copy the file of the class selected by the user
        copyfile(f"resources/class/{player_class}.yaml",
            f"data/players/{ID}.yaml")
        # Print the created player's ID
        print(f"\nCreated new player -> {ID}")
        # Construct the player
        return Player.deserialize(ID)

    @staticmethod
    #
    def deserialize(ID: int):
        # We create a new instance of Player
        player = Player()
        # Fetch the player's informations
        player_data = Utils.import_data_from(f"data/players/{ID}.yaml")

        player.id = ID

        player.role = player_data["role"]
        player.level = player_data["level"]
        player.experience = player_data["experience"]
        player.max_experience = player_data["max experience"]

        player.health = player_data["statistics"]["health"]
        player.max_health = player_data["statistics"]["max health"]
        player.energy = player_data["statistics"]["energy"]
        player.max_energy = player_data["statistics"]["max energy"]

        player.strength = player_data["statistics"]["strength"]
        player.resistance = player_data["statistics"]["resistance"]
        player.intelligence = player_data["statistics"]["intelligence"]
        player.knowledge = player_data["statistics"]["knowledge"]

        player.gold = player_data["gold"]

        print(f"Deserialized player -> {ID}")

        return player

    #
    def serialize(self):
        player_data = dict()

        statistics = { "health" : self.health, "max health" : self.max_health,
            "energy" : self.energy, "max energy" : self.max_energy,
            "strength" : self.strength, "resistance" : self.resistance,
            "intelligence" : self.intelligence, "knowledge" : self.knowledge }

        player_data["role"] = self.role
        player_data["level"] = self.level
        player_data["experience"] = self.experience
        player_data["max experience"] = self.max_experience

        player_data["statistics"] = statistics

        player_data["gold"] = self.gold

        print(f"Serialized player -> {self.id}")
        Utils.write_data_to(f"data/players/{self.id}.yaml", player_data)

    def informations(self, this_player):
        # Build the embed message
        new_message = Embed(title=f"{self.role.capitalize()} | niveau {self.level}", color=0xff9300)
        # Add fields to the message
        new_message.set_author(name=this_player.display_name, icon_url=this_player.avatar_url)
        new_message.add_field(name=f"Vie : {self.health} / {self.max_health}", value="Survivre aux attaques", inline=True)
        new_message.add_field(name=f"Énergie : {self.energy} / {self.max_energy}", value="Lancer des sorts", inline=True)
        new_message.add_field(name=f"Expérience : {self.experience} / {self.max_experience}", value="Monter en niveau", inline=True)
        new_message.add_field(name=f"Force : {self.strength}", value="Attaques physiques", inline=True)
        new_message.add_field(name=f"Intelligence : {self.intelligence}", value="Attques magiques", inline=True)
        new_message.add_field(name=f"Esquive : 2", value="Éviter des attaques", inline=True)
        new_message.add_field(name=f"Resistance : {self.resistance}", value="Moins de dégats physiques", inline=True)
        new_message.add_field(name=f"Savoir : {self.knowledge}", value="Moins de dégats magiques", inline=True)
        new_message.add_field(name=f"Or : {self.gold}", value="Acheter des objets", inline=True)
        # Return the final embed message
        return new_message
