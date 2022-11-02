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
        return self.__class__.__objects

    def new(self, obj):
        "add a new object"
        if obj:
            key = "{0}.{1}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj
        else:
            raise AttributeError

    def save(self):
        "serialize the object"
        if re.search("[\\w\\d]*.json", self.__file_path):
            with open(self.__file_path, mode="w",
                        encoding="utf-8") as myfile:
                if self.__objects:
                    dic_t = {}
                    for i, j in self.__objects.items():
                        if isinstance(j, BaseModel):
                            dic_t[i] = j.to_dict()
                    json.dump(dic_t, myfile)

    def reload(self):
        "deserialize the object"
        if exists(FileStorage.__file_path) and getsize(FileStorage.
                                                       __file_path) > 0:
            if re.search("[\\w\\d]*.json", FileStorage.__file_path):
                with open(FileStorage.__file_path, mode="r") as myfile:
                    objs = json.load(myfile).values()
                    for obj in objs:
                        eval(obj["__class__"])(**obj)
