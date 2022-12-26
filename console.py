#!/usr/bin/python3
'''Entry point of the command interpreter
'''
import cmd
import json
import re

import models
from models import BaseModel, User, State, \
    City, Amenity, Place, Review


def isfloat(s):
    '''Checks if a string is a decimal'''
    try:
        float(s)
        return True
    except ValueError:
        return False
