# utils.py
import yaml

class Utils():

    @staticmethod
    # Imports and returns a dictionary of data. The data read from the file
    # whose path is specified to the method as an argument.
    def import_data_from(path: str) -> dict:
        # Load the data from the file
        with open(path, mode='r') as file:
             dictionary = yaml.full_load(file)
        # Return the dictionary of data
        return dictionary
