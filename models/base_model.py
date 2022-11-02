#!/usr/bin/python3
"define a class BaseModel"
import uuid
from datetime import datetime
import models


class BaseModel:
    "define some attributes and Getter/Setter"

    def __init__(self, *args, **kwargs):
        "initializing the attributes required"

        iso_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for i, j in kwargs.items():
                if i in ['created_at', 'updated_at']:
                    self.__dict__[i] = datetime.strptime(j, iso_format)
                else:
                    self.__dict__[i] = j
        else:
            self.id = uuid.uuid4().hex
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        "update the attribute 'updated_at'"
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        return "[{0}] ({1}) {2}".format(self.__class__.__name__,
                                        self.id, self.__dict__)

    def to_dict(self):
        "return instance as dictionary"
        dictn = self.__dict__.copy()
        dictn["__class__"] = self.__class__.__name__
        dictn["created_at"] = self.created_at.isoformat()
        dictn["updated_at"] = self.updated_at.isoformat()
        return dictn
