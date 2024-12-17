from managers.states import GameState
from core.constants import *
import pygame


class SettingState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.settings = self.game.settings  
        self.selected_option = 0
        self.settings_list = [
            ("Asteroid Spawn Rate", self.settings.spawn_rate_range),
            ("Player Speed", self.settings.player_speed_range),
            ("Asteroid Min Radius", self.settings.asteroid_radius_range)
        ]

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 48)
        y_offset = 100

        # Draw title
        title = font.render("Settings", True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

        # Draw each setting
        for i, (setting_name, (min_val, max_val, step)) in enumerate(self.settings_list):
            # Determine which value we're working with
            if i == 0:
                current_value = self.settings.asteroid_spawn_rate
            elif i == 1:
                current_value = self.settings.player_speed
            else:
                current_value = self.settings.asteroid_min_radius

            # Setting name
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            text = font.render(f"{setting_name}: {current_value}", True, color)
            text_pos = (SCREEN_WIDTH // 4, y_offset + i * 100)
            screen.blit(text, text_pos)

            # Draw slider
            slider_length = 400
            slider_pos = (SCREEN_WIDTH // 4 + 50, y_offset + i * 100 + 40)
            pygame.draw.line(screen, (128, 128, 128), 
                           slider_pos, 
                           (slider_pos[0] + slider_length, slider_pos[1]), 
                           2)

            # Draw slider position
            normalized_pos = (current_value - min_val) / (max_val - min_val)
            slider_button_x = slider_pos[0] + normalized_pos * slider_length
            pygame.draw.circle(screen, color,
                             (int(slider_button_x), slider_pos[1]),
                             8)

        # Draw instructions
        instructions = font.render("Press ESC to return to menu", True, (255, 255, 255))
        screen.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, 
                                 SCREEN_HEIGHT - 100))


    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameState.create_state("menu", self.game)
                elif event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.settings_list)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.settings_list)
                elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self._adjust_setting(event.key == pygame.K_RIGHT)
        return self

    def _adjust_setting(self, increase):
        setting_name, (min_val, max_val, step) = self.settings_list[self.selected_option]
        
        # Get current value based on selected option
        if self.selected_option == 0:
            current = self.settings.asteroid_spawn_rate
            new_val = current + (step if increase else -step)
            self.settings.asteroid_spawn_rate = max(min_val, min(max_val, new_val))
        elif self.selected_option == 1:
            current = self.settings.player_speed
            new_val = current + (step if increase else -step)
            self.settings.player_speed = max(min_val, min(max_val, new_val))
        else:
            current = self.settings.asteroid_min_radius
            new_val = current + (step if increase else -step)
            self.settings.asteroid_min_radius = max(min_val, min(max_val, new_val))