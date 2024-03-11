#!/usr/bin/python3
"""I used this module to define a sub class that
will inherit form the BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class will  add more attriburtes to the instance"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
