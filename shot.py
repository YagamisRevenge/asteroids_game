from circleshape import *
import pygame

class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)