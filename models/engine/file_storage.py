#!/usr/bin/python3
""" Creation to define attrs methods of the console """
import json
from os import path
from models.base_model import BaseModel
"""from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
           "State": State, "City": City, "Amenity": Amenity, "Review": Review}"""


classes = {"BaseModel": BaseModel}


class FileStorage:
    """ defines attrs / methods """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return objects """
        return self.__objects

    def new(self, obj):
        """ sets in '__objects' the obj with key """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to JSON file through creating dict """
        dict_data = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(dict_data, file)

    def reload(self):
        """ deserializes JSON file  to  __objects """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_data = file.read()
                obj_dict = json.loads(json_data)

            for key, value in obj_dict.items():
                class_name = value["__class__"]
                cls = classes[class_name]
                obj = cls(**value)
                self.__objects[key] = obj
