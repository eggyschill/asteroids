import sys
import os
import pygame
import time
import socket
import threading

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.constants import *
from core.circleshape import *
from entities.player import *
from entities.asteroid import *
from managers.asteroidfield import *


def main():
    pygame.init()    # Initialize pygame

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF) # Set screen (display) width and height
    clock = pygame.time.Clock() # Creating clock object for time tracking, and delta time variable

    updateable_group = pygame.sprite.Group() # Creating groups to store updateable_groups and drawable_groups
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updateable_group, drawable_group) # Creating static field 
    Asteroid.containers = (asteroids_group, updateable_group, drawable_group) # Creating static field for asteroid
    AsteroidField.containers = updateable_group
    Shot.containers = (drawable_group, updateable_group, shots_group)
    
    # Instantiate player and asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Initial player object
    player_ref = [player]  # Use a list to store the player as a mutable reference
    asteroidField = AsteroidField(asteroids_group, updateable_group, drawable_group) 
    gameState = GameState.RUNNING
    dt = 0

    # Start the listener thread and pass the mutable player reference
    listener_thread = threading.Thread(target=listen_for_shoot_commands, args=(player_ref,))
    listener_thread.daemon = True  # Ensures the thread closes with the main program
    listener_thread.start()

    # Game loop
    while True:
        if gameState == GameState.RUNNING:
            for event in pygame.event.get():  # Check for quit event
                if event.type == pygame.QUIT:
                    return
            
            screen.fill((0, 0, 0))  # Clear the screen to black before drawing

            for obj in updateable_group:
                obj.update(dt) # Update all instances of updateable_group groups

            for asteroid in asteroids_group:
                # Check for player-asteroid collision
                if pygame.sprite.collide_circle(player_ref[0], asteroid):
                    print("Collision detected with player, asteroid")
                    gameState = GameState.GAME_OVER
                # Check for shot-asteroid collision
                for shot in shots_group:
                    if pygame.sprite.collide_circle(shot, asteroid):
                        shot.kill()  # Destroy the shot
                        asteroid.split()  # Split the asteroid upon collision

            for obj in drawable_group:
                obj.draw(screen) # Draw all drawable groups to the screen
                        
            pygame.display.flip()  # Update the display with the newly drawn frame
            
            dt = clock.tick(60) / 1000  # Calculate delta time (in seconds) and cap the FPS at 60

        elif gameState == GameState.GAME_OVER:
            # Show "Game Over" message or wait for player to restart
            screen.fill((0, 0, 0))
            game_over_font = pygame.font.Font(None, 74)
            game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    # Restart the game and update the player reference
                    asteroidField, player_ref[0] = restart_game(updateable_group, drawable_group, asteroids_group, shots_group)
                    gameState = GameState.RUNNING


class GameState():
    RUNNING = 1
    GAME_OVER = 2

def restart_game(updateable_group, drawable_group, asteroids_group, shots_group):
    # Clear all groups
    updateable_group.empty()
    drawable_group.empty()
    asteroids_group.empty()
    shots_group.empty()
    # Re-instantiate the player and asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Player will be added to updateable_group and drawable_group
    asteroidField = AsteroidField(asteroids_group, updateable_group, drawable_group)  # asteroids will be added to their groups automatically
    return asteroidField, player

    
def listen_for_shoot_commands(player_ref):
    HOST = "localhost"
    PORT = 44444

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # open socket tunneling to this server
        s.bind((HOST, PORT))
        s.listen()
        print("Game server listening to commands")

        conn, addr = s.accept()  # Accept Pi5 commands
        print(f"Connection from {addr} established")
        with conn:
            while True:
                data = conn.recv(1024)
                if data == b"SHOOT":
                    player_ref[0].should_shoot = True
                    print("Received SHOOT command, setting should_shoot to True")  # Debug statement
                    print(f"Status : {player_ref[0].should_shoot}")  # Verify that should_shoot is set correctly


if __name__ == "__main__":
    main()
