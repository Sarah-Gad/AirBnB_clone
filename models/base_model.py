#!/usr/bin/python3
"""I used this module to define the base class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """i sued this class to define the common
    attri and methods for the other classes"""

    def __init__(self, *args, **kwargs):
        """this method is the constuctor method to make instance"""
        if (len(kwargs) != 0):
            for k_k, k_v in kwargs.items():
                if (k_k == "__class__"):
                    continue
                if (k_k == "created_at" or k_k == "updated_at"):
                    setattr(self, k_k, datetime.strptime(
                        k_v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k_k, k_v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """I override this method to control the
        string representaion of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """I uwd this method to update the instance
        attribute updated_at with the curr time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """I used this method to return the dict that
        contains all the key_values of the __dict__
        instance"""
        att_dict = {}
        for ins_k, ins_v in self.__dict__.items():
            if ins_k == "created_at" or ins_k == "updated_at":
                d_t_con = ins_v.isoformat()
                att_dict[ins_k] = d_t_con
            else:
                att_dict[ins_k] = ins_v
        att_dict["__class__"] = self.__class__.__name__
        return att_dict
