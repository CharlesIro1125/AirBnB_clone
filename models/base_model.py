#!/usr/bin/python3
import uuid
from datetime import datetime
"""Defines a Base Class BaseModel"""
class BaseModel:
    """class BaseModel from which all other classes inherit"""
    def __init__(self, id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now()):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
    def __str__(self):
        string = f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
        return string

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        d = self.__dict__
        d["__class__"] = __class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
