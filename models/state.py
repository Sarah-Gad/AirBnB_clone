#!/usr/bin/python3
"""I used this module to define a sub class of the parent
basmodel class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class added a newname attri"""
    name = ""
