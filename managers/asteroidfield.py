import pygame
import random
from entities.asteroid import Asteroid
from core.constants import *
from core.gamesettings import GameSettings


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self, game, asteroids_group, updateable_group, drawable_group):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.asteroids_group = asteroids_group
        self.updateable_group = updateable_group
        self.drawable_group = drawable_group
        self.game = game

    # method for spawning individual asteroid and setting it's velocity
    def spawn(self, radius, position, velocity): 
        asteroid = Asteroid(self.game, position.x, position.y, radius)
        asteroid.velocity = velocity
        self.asteroids_group.add(asteroid)
        self.updateable_group.add(asteroid)
        self.drawable_group.add(asteroid)

    # asteroidfield update method
    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > self.game.settings.asteroid_spawn_rate:
            self.spawn_timer = 0

            # Spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            
            # This creates a new asteroid and assigns it to the correct position and velocity
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity) 
