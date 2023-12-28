"""This module stores a class for managing a dictionary of users
who each have a dictionary for user data.
The dictionary of users is stored in a JSON file.
"""


import json
import tool


class Session():
    def __init__(self, file_name):
        """This initializes the instance with a dictionary of users from
        a file if it exists, a run flag, and no user logged in.
        """
        self.running = True
        self.key = None
        self.key_value = None
        self.target_file = file_name
        try:
            with open(file_name) as file_object:
                data_dict = json.load(file_object)
        except FileNotFoundError:
            self.data = {}
        else:
            self.data = data_dict

    def save(self):
        """This method writes the session data to the target file."""
        with open(self.target_file, 'w') as file_object:
            json.dump(self.data, file_object, indent=4, sort_keys=True)

    def end(self):
        """This method sets the session run flag to False and
        prints a message.
        """
        self.running = False
        print('\nExiting program.')
