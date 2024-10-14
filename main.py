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
    while (True):
        for event in pygame.event.get():        # Setting parameter for quitting the program
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))          # Otherwise, fill the screen with black
        player1.draw(screen)            # Draw the player on the screen per iteration
        pygame.display.flip()         # Update the display at 60 FPS, store that in a delta time variable in seconds
        dt = clock.tick(60) / 1000  


if __name__ == "__main__":
    main()