#!/usr/bin/python3
'''
Represents amenity class  that inherits from BaseModel
'''
from models.base_model import BaseModel


class Amenity (BaseModel):
    '''
        Represents Class Amenity with public class attribute
    '''
    name = ""
