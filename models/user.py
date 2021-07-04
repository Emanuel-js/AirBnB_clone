#!/usr/bin/python3
'''
    Represents an user class  that inherits from BaseModel
'''

from models.base_model import BaseModel


class User(BaseModel):
    '''
        Repretesents Class User with public class attribute
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
