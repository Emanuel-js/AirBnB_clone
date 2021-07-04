#!/usr/bin/python3
'''
    Represents a BaseModel class
'''
import models
import uuid
from datetime import datetime


class BaseModel():
    '''
        BaseModel class defines all common attributes/methods
        for other classes
    '''
    def __init__(self, *args, **kwargs):
        '''
            instanciation of a new instance
            Args:
                id: id of the new instance
                created_at: current datetime
                updated_at: update the current datetime
        '''
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    (self.__dict__)[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
            method to print the str representation of an instance
        '''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
            method to update the current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
            set the value of the atributtes of an instance and
            convert the created_at and updated_at atrributes to
            isoformat method and convert in a new dictionary
            add key "__class__" to dictionary and set the class name of
            an instance
        '''
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
