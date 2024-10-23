import pygame
from core.circleshape import CircleShape
from core.constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        super().update(dt)
    
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            random_angle = random.uniform(20,50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_one.velocity = new_vector1 * 1.2
            split_asteroid_two.velocity = new_vector2 * 1.2