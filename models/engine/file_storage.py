#!/usr/bin/python3
"""I used this module to make the FileStorage class
that I will usefor serialization and deserialization"""

import json
from models.base_model import BaseModel
from os.path import exists


class FileStorage:
    """I will use this class to save instances into a json file
    and also to get instances from a json file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method will return the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """This method is used to set the __object"""
        thek = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[thek] = obj

    def save(self):
        """This method will serialize the ___object"""
        detailed = {}
        for k_ob, v_ob in FileStorage.__objects.items():
            detailed[k_ob] = v_ob.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as jjf:
            json.dump(detailed, jjf)

    def reload(self):
        """This method is used to desialize the json file
        that contains the serialized dict"""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as jjf:
                deser = json.load(jjf)
            for o_v in deser.values():
                c_name = o_v["__class__"]
                if isinstance(c_name, str) and type(eval(c_name)) == type:
                    self.new(eval(c_name)(**o_v))
        except FileNotFoundError:
            pass
