# Add to core/settings.py (new file)
from core.constants import *

class GameSettings:
    def __init__(self):
        # Initialize with default values from constants
        self.asteroid_spawn_rate = ASTEROID_SPAWN_RATE
        self.player_speed = PLAYER_SPEED
        self.asteroid_min_radius = ASTEROID_MIN_RADIUS
        
        # Define limits for each setting
        self.spawn_rate_range = (1, 10, 1)  # (min, max, step)
        self.player_speed_range = (100, 500, 100)
        self.asteroid_radius_range = (10, 50, 5)