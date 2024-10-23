import pygame
from core.circleshape import CircleShape
from core.constants import *
from entities.shot import *

class Player(CircleShape):  
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.PLAYER_SHOT_TIMER = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255), self.triangle(), 2)
        pygame.draw.circle(screen, (255,0,0), self.rect.center, self.radius, 1) # red circle for debugging

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        super().update(dt)
        print(f"Player position: {self.position}, rect: {self.rect}, radius: {self.radius}") # debugging
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.PLAYER_SHOT_TIMER -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if (self.PLAYER_SHOT_TIMER <= 0):
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.PLAYER_SHOT_TIMER = PLAYER_SHOOT_COOLDOWN
        
        

        
            