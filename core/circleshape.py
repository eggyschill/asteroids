import pygame
from core.constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        # Adding pygame rect attribute for proper hitbox handling
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # updating position of entity 
        self.position += self.velocity * dt
        # updating hitbox position
        self.rect.center = (self.position.x, self.position.y)


        # collision detection

