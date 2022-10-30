#!/usr/bin/python3
"define a FileStorage class"
import json
from models.base_model import BaseModel
import re
from os.path import exists, getsize


class FileStorage:
    "creating a FIleStorage class"

    __file_path = ""
    __objects = {}

    def __init__(self, path=""):
        FileStorage.__file_path = path

    def all(self):
        return self.__class__.__objects

    def new(self, obj):
        "add a new object"
        if obj:
            key = "{0}.{1}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        "serialize the object"
        if exists(FileStorage.__file_path):
            if re.search("[\\w\\d]*.json", FileStorage.__file_path):
                with open(FileStorage.__file_path, mode="w",
                          encoding="utf-8") as myfile:
                    if FileStorage.__objects:
                        dic_t = {}
                        for i, j in FileStorage.__objects.items():
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
