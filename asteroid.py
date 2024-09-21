from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroids(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        type_options = ["small","medium","large"]
        self.type = type_options[random.randrange(0,len(type_options)-1)]

    def draw(self, screen):
        pygame.draw.circle(screen, "White",self.position,self.radius, 2)

    def update(self,dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        vector_1 = self.velocity.rotate(rand_angle)
        vector_2 = self.velocity.rotate((rand_angle*-1))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroids(self.position.x,self.position.y,new_radius)
        ast_2 = Asteroids(self.position.x,self.position.y,new_radius)
        ast_1.velocity = 1.2 * (vector_1)
        ast_2.velocity = 1.2 * (vector_2)
