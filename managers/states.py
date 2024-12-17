from abc import ABC, abstractmethod
import pygame
from core.constants import *
from enum import Enum, auto

class GameStates(Enum):
    MENU = auto()
    RUNNING = auto()
    PAUSED = auto()
    SETTINGS = auto()
    GAME_OVER = auto()
    HIGH_SCORES = auto()

class GameState(ABC):
    def __init__(self, game):
        self.game = game

    @staticmethod
    def create_state(state_name, game):
        if state_name == "menu":
            from managers.menustate import MenuState
            return MenuState(game)
        elif state_name == "running":
            from managers.runningstate import RunningState
            return RunningState(game)
        elif state_name == "settings":
            from managers.settingstate import SettingState
            return SettingState(game)
        elif state_name == "highscores":  
            from managers.highscorestate import HighScoreState
            return HighScoreState(game)
        
    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self, dt):
        # return next state or None if no change
        pass

    @abstractmethod
    def handle_input(self, event):
        # return next state of none if no change
        pass
    