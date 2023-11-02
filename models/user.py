#!/usr/bin/python3
"""Class User that inherites from BaseModel"""


from models.base_model import BaseModel
import email


class User(BaseModel):
    "Definition of the class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
