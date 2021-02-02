# players.py
import yaml
from source.utils import Utils

class Players():

    @staticmethod
    # Returns an array of Players() built from the
    # data in resources/players.yaml and resources/players/*
    def get_array() -> dict:
        players = dict()

        # Get the players' name from a file
        names = Utils.import_data_from("resources/players.yaml")

        # Ensure names is a non empty dictionary
        if bool(names):
            for name in names:
                # Add the discord user ID to the players dict with its
                # corresponding Player instance
                players[name] = Players.deserialize(name)
        return players
