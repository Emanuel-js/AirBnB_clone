#!/usr/bin/python3
'''
    Represents a city class  that inherits from BaseModel
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
        Represent a city class
        Args:
        state_id: string - empty string: it will be the State.id
        name: empty string
    '''
    state_id = ""
    name = ""
