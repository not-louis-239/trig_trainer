from typing import TYPE_CHECKING

import pygame as pg
from pygame.event import Event
from pygame.key import ScancodeWrapper

from .base import State

if TYPE_CHECKING:
    from trig_trainer.game import Game

class MenuState(State):
    def __init__(self, game: Game) -> None:
        pass

    def reset(self) -> None:
        pass

    def take_input(self, keys: ScancodeWrapper, events: list[Event], dt_s: float) -> None:
        pass

    def update(self, dt_s: float) -> None:
        pass

    def draw(self, screen: pg.Surface):
        pass
