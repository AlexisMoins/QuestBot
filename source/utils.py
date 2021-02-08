# utils.py
import yaml
from os import walk, path
from discord import Embed

class Utils():

    @staticmethod
    # Import and return a dictionary of data. The data read from the file
    # whose path is specified to the method as an argument.
    def import_data_from(path: str) -> dict:
        # Load the data from the file
        with open(path, mode='r') as file:
             dictionary = yaml.full_load(file)
        # Return the dictionary of data
        return dictionary

    @staticmethod
    # Write data given to the method into the specified file
    def write_data_to(path: str, data: dict):
        # Write data to the file
        with open(path, mode='w') as file:
            dictionary = yaml.dump(data, file)

    @staticmethod
    # Return the list of all the files present in the directory (path) given
    # to the method
    def get_filenames_from(path: str) -> list:
        # Prepare an empty list
        files = list()
        # Get the filenames
        for (_, _, filenames) in walk(path):
            files.extend(filenames)
        # Return the list of files
        return files

    @staticmethod
    # Return the player list built from a list of filenames
    def get_player_list() -> list:
        # Fetch the list of the players
        files = Utils.get_filenames_from("data/players/")
        # Prepare an empty list
        player_list = list()
        for file in files:
            # Get the IDs by removing the file's extension
            player_ID = path.splitext(file)[0]
            player_list.append(player_ID)
            # Return the player list
        return player_list

    @staticmethod
    # Return true if the ID given to the method is in the player list
    def player_exists(ID: int) -> bool:
        # Get the player list
        player_list = Utils.get_player_list()

        if str(ID) in player_list:
            return True
        return False

    @staticmethod
    # Return a discord.Embed object representing the formated message
    def build_message(message_name: str):
        # Get the embed message data
        msg = Utils.import_data_from("resources/messages.yaml")[message_name]
        # Build the embed message
        new_message = Embed(title=msg["title"], description=msg["description"],
            color=msg["color"])
        # Add fields to the message
        for key, field in msg["fields"].items():
            new_message.add_field(name=field["name"], value=field["value"],
                inline=field["inline"])
        # Return the final embed message
        return new_message
