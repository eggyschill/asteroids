import pygame
from core.circleshape import CircleShape
from core.constants import *
from entities.shot import *

class Player(CircleShape):  
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.should_shoot = False # Flag to check if shots are fired (button integration)
        self.rotation = 0
        self.shot_timer = 0
        self.PLAYER_SHOT_TIMER = 0

    # triangle, position for drawing
    def triangle(self, position=None):
        # If no position is provided, use the player's current position
        if position is None:
            position = self.position
        
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = position + forward * self.radius
        b = position - forward * self.radius - right
        c = position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen):
        # Normal drawing
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        
        # Check if the player is near the right edge and draw them on the left as well
        if self.position.x + self.radius > SCREEN_WIDTH:
            offset_position = pygame.Vector2(self.position.x - SCREEN_WIDTH, self.position.y)
            pygame.draw.polygon(screen, (255, 255, 255), self.triangle(offset_position), 2)

        # Check if the player is near the left edge and draw them on the right as well
        if self.position.x - self.radius < 0:
            offset_position = pygame.Vector2(self.position.x + SCREEN_WIDTH, self.position.y)
            pygame.draw.polygon(screen, (255, 255, 255), self.triangle(offset_position), 2)

        # Check if the player is near the bottom edge and draw them at the top as well
        if self.position.y + self.radius > SCREEN_HEIGHT:
            offset_position = pygame.Vector2(self.position.x, self.position.y - SCREEN_HEIGHT)
            pygame.draw.polygon(screen, (255, 255, 255), self.triangle(offset_position), 2)

        # Check if the player is near the top edge and draw them at the bottom as well
        if self.position.y - self.radius < 0:
            offset_position = pygame.Vector2(self.position.x, self.position.y + SCREEN_HEIGHT)
            pygame.draw.polygon(screen, (255, 255, 255), self.triangle(offset_position), 2)

        # pygame.draw.circle(screen, (255,0,0), self.rect.center, self.radius, 1) # red circle for debugging

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        super().update(dt)
        if (self.should_shoot):
            print("self.shoot is true, shooting")
            self.shoot()
            self.should_shoot = False # reset flag 
        if (self.position.x > SCREEN_WIDTH or 
            self.position.x < 0 or 
            self.position.y > SCREEN_HEIGHT or 
            self.position.y < 0) :
                self.position.x = self.position.x % SCREEN_WIDTH
                self.position.y = self.position.y % SCREEN_HEIGHT        
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
            print(f"shot flag status : {self.should_shoot}")
        self.PLAYER_SHOT_TIMER -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if (self.PLAYER_SHOT_TIMER <= 0):
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.PLAYER_SHOT_TIMER = PLAYER_SHOOT_COOLDOWN
        
        

        
            