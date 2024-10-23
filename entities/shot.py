import pygame
from core.circleshape import CircleShape
from core.constants import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.shot_radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.shot_radius, 2)

    def update(self, dt):
        super().update(dt)