#!/usr/bin/python3i
"""a class named FileStorage"""
import json
from models.base_model import BaseModel
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all objects"""
        return self.__objects

    def new(self, obj):
        """creates new object"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
    """
    def to_dict(self):
        d = self.__dict__
        d["__class__"] = __class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d 
    """
    def save(self):
        """saves objexts in a json file"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """initializes the reload function to open storage files"""
        try:
            with open(self.__file_path, 'r') as f:
                load = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass
