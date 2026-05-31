from typing import TYPE_CHECKING

import pygame as pg
from pygame.event import Event
from pygame.key import ScancodeWrapper

from .base import State

if TYPE_CHECKING:
    from trig_trainer.game import Game

class GameState(State):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.total_questions = 0
        self.correct_questions = 0

    def reset(self) -> None:
        self.total_questions = 0
        self.correct_questions = 0

    def take_input(self, keys: ScancodeWrapper, events: list[Event], dt_s: float) -> None:
        pass

    def update(self, dt_s: float):
        pass

    def draw(self, screen: pg.Surface):
        screen.fill((0, 0, 0))
