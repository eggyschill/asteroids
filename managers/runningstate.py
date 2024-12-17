import pygame
from core.constants import *
from managers.states import GameState



class RunningState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.paused = False
        self.game_over = False
        self.score = 0
        self.survival_timer = 0
        
    def update(self, dt):
        if self.paused or self.game_over:
            return
        
        # Update survival score (10 points per second)
        self.survival_timer += dt
        self.score += int(10 * dt)  # Convert to int to avoid floating point scores

        # Update all game objects
        for obj in self.game.updateable_group:
            obj.update(dt)
            
        # Check collisions
        for asteroid in self.game.asteroids_group:
            if pygame.sprite.collide_circle(self.game.player, asteroid):
                self.handle_game_over()
            for shot in self.game.shots_group:
                if pygame.sprite.collide_circle(shot, asteroid):
                    shot.kill()
                    # Award points based on asteroid size
                    points = int((asteroid.radius / self.game.settings.asteroid_min_radius) * 100)
                    self.score += points
                    asteroid.split()

                
    def draw(self, screen):
        screen.fill((0, 0, 0))
        
        # Draw all game objects
        for obj in self.game.drawable_group:
            obj.draw(screen)
            
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 20, 20))
            
        if self.paused:
            font = pygame.font.Font(None, 74)
            text = font.render("PAUSED", True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
            
        if self.game_over:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
            score_text = font.render(f"Final Score: {self.score}", True, (255, 255, 255))
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 80))
            
            
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.game_over:
                        return GameState.create_state("menu", self.game)
                    self.paused = not self.paused
                    return self
                elif event.key == pygame.K_r and self.game_over:
                    return RunningState(self.game)
        return self 

    def handle_game_over(self):
        self.game_over = True
        # Check if this is a high score
        self.game.check_high_score(self.score)