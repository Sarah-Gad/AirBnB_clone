#!/usr/bin/python3
"""This mudule defines a child sub class of
the parent basemodel class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class adds the review attri"""
    place_id = ""
    user_id = ""
    text = ""
