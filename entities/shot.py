import pygame
from core.circleshape import CircleShape
from core.constants import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.shot_radius = SHOT_RADIUS
        self.shot_travel_distance = 0

    def draw(self, screen):
        # Draw the shot at its current position
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
        
        # Optionally, handle wrap-around drawing if shots are large enough
        if self.position.x + self.radius > SCREEN_WIDTH:
            offset_position = pygame.Vector2(self.position.x - SCREEN_WIDTH, self.position.y)
            pygame.draw.circle(screen, (255, 255, 255), (offset_position.x, offset_position.y), self.radius, 2)
        
        if self.position.x - self.radius < 0:
            offset_position = pygame.Vector2(self.position.x + SCREEN_WIDTH, self.position.y)
            pygame.draw.circle(screen, (255, 255, 255), (offset_position.x, offset_position.y), self.radius, 2)

        if self.position.y + self.radius > SCREEN_HEIGHT:
            offset_position = pygame.Vector2(self.position.x, self.position.y - SCREEN_HEIGHT)
            pygame.draw.circle(screen, (255, 255, 255), (offset_position.x, offset_position.y), self.radius, 2)
        
        if self.position.y - self.radius < 0:
            offset_position = pygame.Vector2(self.position.x, self.position.y + SCREEN_HEIGHT)
            pygame.draw.circle(screen, (255, 255, 255), (offset_position.x, offset_position.y), self.radius, 2)

    def update(self, dt):
        super().update(dt)
        if (self.shot_travel_distance >= 800) :
            self.kill()
        # Applying wrapping logic to bullets
        if (self.position.x > SCREEN_WIDTH or 
            self.position.x < 0 or 
            self.position.y > SCREEN_HEIGHT or 
            self.position.y < 0) :
                self.position.x = self.position.x % SCREEN_WIDTH
                self.position.y = self.position.y % SCREEN_HEIGHT
        self.shot_travel_distance += PLAYER_SHOOT_SPEED * dt
