#!/usr/bin/python3
'''
Represents  Review  class  that inherits from BaseModel
'''
from models.base_model import BaseModel


class Review (BaseModel):
    '''
        Represents Class Review  with public class attribute
    '''
    place_id = ""
    user_id = ""
    text = ""
