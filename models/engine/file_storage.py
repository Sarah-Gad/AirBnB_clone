#!/usr/bin/python3
"""I used this module to make the FileStorage class
that I will usefor serialization and deserialization"""


class FileStorage:
    """I will use this class to save instances into a json file
    and also to get instances from a json file"""

    __file_path = "models/engine/the_json_file.json"
    __objects = {}

    def all(self):

