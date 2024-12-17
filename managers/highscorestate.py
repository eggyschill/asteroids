# Create a new file: managers/highscorestate.py
import pygame
from managers.states import GameState
from core.constants import *

class HighScoreState(GameState):
    def __init__(self, game):
        super().__init__(game)
        
    def update(self, dt):
        pass
        
    def draw(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        title = font.render("High Scores", True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        
        scores = self.game.high_scores.get_scores()
        score_font = pygame.font.Font(None, 48)
        
        for i, score in enumerate(scores):
            text = score_font.render(f"{i+1}. {score}", True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 250 + i * 60))
            
        instruction = score_font.render("Press ESC to return", True, (255, 255, 255))
        screen.blit(instruction, (SCREEN_WIDTH // 2 - instruction.get_width() // 2, SCREEN_HEIGHT - 100))
            
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return GameState.create_state("menu", self.game)
        return self