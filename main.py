import pygame
from constants import *
from player import *


def main():
    pygame.init()    # Initialize pygame

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set screen (display) width and height
    
    clock = pygame.time.Clock() # Creating clock object for time tracking, and delta time variable
    dt = 0

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)# Instantiate player object

    # Gane loop, infinite
    while True:
        for event in pygame.event.get():  # Check for quit event
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))  # Clear the screen to black before drawing
        
        player1.update(dt)  # Update the player's state (e.g., movement, rotation)
        player1.draw(screen)  # Draw the player to the screen
        
        pygame.display.flip()  # Update the display with the newly drawn frame
        
        dt = clock.tick(60) / 1000  # Calculate delta time (in seconds) and cap the FPS at 60



if __name__ == "__main__":
    main()