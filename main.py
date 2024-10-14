import pygame
from constants import *


def main():
    # Initialize pygame
    pygame.init()
    # Set screen (display) width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Creating clock object for time tracking, and delta time variable
    clock = pygame.time.Clock()
    dt = 0

    # Gane loop, infinite
    while (True):
        # Setting parameter for quitting the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Otherwise, fill the screen with black
        screen.fill((0, 0, 0))  
        # Update the display at 60 FPS, store that in a delta time variable in seconds
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()