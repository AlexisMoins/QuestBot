# players.py
import yaml
from .utils import Utils

class Players():

    @staticmethod
    # Returns an array of Players() built from the data in the resources folder
    def get_array() -> dict:
        players = dict()
        # Get the players' ID from a file
        ID_list = Utils.import_data_from("resources/players.yaml")

        # Ensure names is a non empty dictionary
        if bool(ID_list):
            for ID in ID_list:
                # Add the discord user ID to the players dict with its
                # corresponding Player instance
                players[ID] = Players.deserialize(ID)
        return players
