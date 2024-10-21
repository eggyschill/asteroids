import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()    # Initialize pygame

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set screen (display) width and height
    
    clock = pygame.time.Clock() # Creating clock object for time tracking, and delta time variable

    updateable = pygame.sprite.Group() # Creating groups to store updateables and drawables
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable) # Creating static field 
    Asteroid.containers = (asteroids, updateable, drawable) # Creating static field for asteroid
    AsteroidField.containers = (updateable)
    Shot.containers = (drawable, updateable, shots)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Instantiate player object
    asteroidField = AsteroidField() 

    dt = 0

    # Game loop, infinite
    while True:
        for event in pygame.event.get():  # Check for quit event
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))  # Clear the screen to black before drawing

        for obj in updateable:
            obj.update(dt) # Update all instances of updateable groups

        for obj in asteroids:
            if (player.isColliding(obj)):
                print("Game over!")
                sys.exit("Game over!")
            for shot in shots:
                if (shot.isColliding(obj)):
                    shot.kill()
                    obj.kill()


        for obj in drawable:
            obj.draw(screen) # Draw all drawable groups to the screen
                    
        pygame.display.flip()  # Update the display with the newly drawn frame
        
        dt = clock.tick(60) / 1000  # Calculate delta time (in seconds) and cap the FPS at 60



if __name__ == "__main__":
    main()