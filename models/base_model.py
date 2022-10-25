#!/usr/bin/python3
"define a class BaseModel"
import uuid
from datetime import datetime


class BaseModel:
    "define some attributes and Getter/Setter"

    def __init__(self):
        "initializing the attributes required"

        self.id = uuid.uuid4().hex
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        "update the attribute 'updated_at' "
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{0}] ({1}) {2}".format(self.__class__.__name__,
                                        self.id, self.__dict__)

    def to_dict(self):
        "return instance as dictionary"
        dictn = self.__dict__
        dictn["__class__"] = self.__class__.__name__
        dictn["created_at"] = self.created_at.isoformat()
        dictn["updated_at"] = self.updated_at.isoformat()
        return dictn
