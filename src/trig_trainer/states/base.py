from enum import Enum, auto
from typing import TYPE_CHECKING


import pygame as pg
from pygame import Surface
from pygame.key import ScancodeWrapper


from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from trig_trainer.game import Game


class StateID(Enum):
    MENU = auto()
    GAME = auto()


class State(ABC):
    def __init__(self, game: Game) -> None:
        self.game = game

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, dt_s: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def take_input(self, keys: ScancodeWrapper, events: list[pg.event.Event], dt_s: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw(self, screen: Surface):
        raise NotImplementedError
