import sys
import os
import pygame

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
import sys
import os
from core.constants import *
from entities.player import Player
from entities.asteroid import Asteroid
from entities.shot import Shot
from managers.asteroidfield import AsteroidField
from managers.states import GameState
from managers.menustate import MenuState
from managers.runningstate import RunningState
from managers.settingstate import SettingState


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF) # Set screen (display) width and height
        self.clock = pygame.time.Clock()
        
        # Group containers and specific imports
        from core.gamesettings import GameSettings
        self.settings = GameSettings()
        from managers.highscores import HighScoreManager
        self.high_scores = HighScoreManager()
        self.updateable_group = pygame.sprite.Group()
        self.drawable_group = pygame.sprite.Group()
        self.asteroids_group = pygame.sprite.Group()
        self.shots_group = pygame.sprite.Group()
        
        # Set up container references
        Player.containers = (self.updateable_group, self.drawable_group)
        Asteroid.containers = (self.asteroids_group, self.updateable_group, self.drawable_group)
        Shot.containers = (self.drawable_group, self.updateable_group, self.shots_group)
        AsteroidField.containers = (self.updateable_group)
        
        # Start with menu state
        self.state = MenuState(self)
        
    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000
            
            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                    
            # Update current state
            new_state = self.state.handle_input(events)
            if new_state and new_state != self.state:
                self.state = new_state
                if isinstance(self.state, RunningState):
                    self.reset_game()
                    
            self.state.update(dt)
            self.state.draw(self.screen)
            pygame.display.flip()

    def check_high_score(self, score):
        if self.high_scores.check_score(score):
            self.high_scores.add_score(score)
            
    def reset_game(self):
        # Clear all groups
        self.updateable_group.empty()
        self.drawable_group.empty()
        self.asteroids_group.empty()
        self.shots_group.empty()
        
        # Create new player and asteroid field
        self.player = Player(self, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Pass self (game instance)
        self.asteroid_field = AsteroidField(self, self.asteroids_group, self.updateable_group, self.drawable_group)  # Pass self (game instance)
if __name__ == "__main__":
    game = Game()
    game.run()
