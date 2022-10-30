#!/usr/bin/python3
"define a class BaseModel"
import uuid
from datetime import datetime


class BaseModel:
    "define some attributes and Getter/Setter"

    def __init__(self, *args, **kwargs):
        "initializing the attributes required"
        from models import storage
        if kwargs:
            for i, j in kwargs.items():
                if i == 'id':
                    self.id = j
                elif i == 'created_at':
                    self.created_at = datetime.strptime(j,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif i == 'updated_at':
                    self.updated_at = datetime.strptime(j,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif i != '__class__':
                    self.__dict__[i] = j
        elif args:
            for i in range(len(args)):
                if isinstance(args[i], BaseModel):
                    storage.new(args[i])
        else:
            self.id = uuid.uuid4().hex
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)

    def save(self):
        "update the attribute 'updated_at' "
        from models import storage
        "self.updated_at = datetime.now()"
        storage.save()

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
