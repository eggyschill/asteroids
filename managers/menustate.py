import pygame
from core.constants import *
from managers.states import GameState

class MenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.options = ["Play Game", "High Scores", "Settings", "Quit"]
        self.selected_option = 0
        
    def update(self, dt):
        pass  # Menu might have animations or effects to update
        
    def draw(self, screen):
        screen.fill((0, 0, 0))  # Black background
        font = pygame.font.Font(None, 74)
        
        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            text = font.render(option, True, color)
            position = (SCREEN_WIDTH // 2 - text.get_width() // 2,
                       SCREEN_HEIGHT // 2 - len(self.options) * 40 + i * 80)
            screen.blit(text, position)
            
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    if self.options[self.selected_option] == "Play Game":
                        return GameState.create_state("running", self.game)
                    elif self.options[self.selected_option] == "High Scores":  # Add this condition
                        return GameState.create_state("highscores", self.game)
                    elif self.options[self.selected_option] == "Settings":
                        return GameState.create_state("settings", self.game)
                    elif self.options[self.selected_option] == "Quit":
                        pygame.quit()
                        exit()
        return self