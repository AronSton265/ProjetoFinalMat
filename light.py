import pygame
import numpy as np
from vector3 import *
from quaternion import *
import math

class Light:
    def __init__(self, name):
        self.name = name
        self.position = vector3()
