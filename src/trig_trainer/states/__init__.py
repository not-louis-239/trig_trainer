from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import TYPE_CHECKING

import pygame as pg
from pygame import Surface
from pygame.key import ScancodeWrapper

if TYPE_CHECKING:
    from trig_trainer.game import Game

from . import (
    menu_state,
    game_state
)

MenuState = menu_state.MenuState
GameState = game_state.GameState

class StateID(Enum):
    MENU = auto()
    GAME = auto()

class State(ABC):
    def __init__(self, game: Game) -> None:
        self.game = game

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError

    def update(self, dt: int) -> None:
        pass

    def take_input(self, keys: ScancodeWrapper, events: list[pg.event.Event], dt: int) -> None:
        pass

    def draw(self, wn: Surface):
        pass
