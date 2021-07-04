#!/usr/bin/python3
'''
    Represents a  FileStorage class
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    '''
    Class that serializes instances to a JSON file and deserializes
    JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Method to return the dictionay __object
        '''
        return self.__objects

    def new(self, obj):
        '''
        set a new object with the obj in the key
        '''
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        '''
        Method to serializes __objects to the JSON file
        '''
        dic_objects = {}
        for key, value in self.__objects.items():
            dic_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fd:
            json.dump(dic_objects, fd, indent="")

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''

        file = FileStorage.__file_path
        try:
            with open(file, mode="r", encoding='utf-8') as fd:
                js_dic = json.load(fd)
                for key, value in js_dic.items():
                    FileStorage.__objects[key] = eval(
                        value['__class__'] + '(**value)')
        except FileNotFoundError:
            pass
