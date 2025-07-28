import pygame
import random
from constants import *
from circleshape import CircleShape 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # randomize a angle between 20º and 50º to generate two new asteroids 
            random_angle = random.uniform(20, 50)
            # use the rotate() to create 2 new vectors that corresponds to the two new asteroids 
            vector_asteroid_one = self.velocity.rotate(random_angle)
            vector_asteroid_two = self.velocity.rotate(- random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS # calculate new radius 
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            # multiplier the vector with 1.2 to generate a faster asteroid 
            asteroid_one.velocity = vector_asteroid_one * 1.2 
            asteroid_two.velocity = vector_asteroid_two * 1.2
        

        






