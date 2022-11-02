#!/usr/bin/python3
"define a FileStorage class"
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
import re
from os.path import exists, getsize


class FileStorage:
    "creating a FIleStorage class"

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        "add a new object"
        if obj:
            key = "{0}.{1}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj
        elif not isinstance(obj, BaseModel):
            raise AttributeError

    def save(self):
        "serialize the object"
        with open(self.__file_path, mode="w") as myfile:
            dic_t = {}
            for i, j in self.__objects.items():
                dic_t[i] = j.to_dict()
            "print('saving %s', self.__objects.items())"
            json.dump(dic_t, myfile)

    def reload(self):
        "deserialize the object"
        if exists(self.__file_path) and getsize(self.__file_path) > 0:
            if re.search("[\\w\\d]*.json", self.__file_path):
                with open(self.__file_path, mode="r") as myfile:
                    objs = json.load(myfile).values()

                    for obj in objs:
                        eval(obj["__class__"])(**obj)
