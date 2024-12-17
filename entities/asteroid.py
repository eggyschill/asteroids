import pygame
from core.circleshape import CircleShape
from core.constants import *
import random
from core.gamesettings import GameSettings

class Asteroid(CircleShape):
    def __init__(self, game, x, y, radius):
        self.game = game
        self.original_radius = radius
        super().__init__(x, y, max(radius, game.settings.asteroid_min_radius))
        

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
        pygame.draw.circle(screen, (0,255,0), self.rect.center, self.radius + 2, 1) # green circle for debugging


    def update(self, dt):
        super().update(dt)
    
    def split(self):
        self.kill()
        # Check if this asteroid is at the smallest allowed size for the current settings
        if self.original_radius <= self.game.settings.asteroid_min_radius:
            return
        else:
            random_angle = random.uniform(20,50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            
            # Calculate new radius relative to the original radius and minimum size
            new_radius = self.original_radius - self.game.settings.asteroid_min_radius
            
            # Create new asteroids with the calculated radius
            split_asteroid_one = Asteroid(self.game, self.position.x, self.position.y, new_radius)
            split_asteroid_two = Asteroid(self.game, self.position.x, self.position.y, new_radius)
            
            split_asteroid_one.velocity = new_vector1 * 1.2
            split_asteroid_two.velocity = new_vector2 * 1.2