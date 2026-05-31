from typing import TYPE_CHECKING

import pygame as pg
from pygame.event import Event
from pygame.key import ScancodeWrapper

from .base import State
from ..text_input_manager import TextInputManager
from ..utils import draw_text
from ..constants import WN_W, WN_H

if TYPE_CHECKING:
    from trig_trainer.game import Game

class GameState(State):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.total_questions = 0
        self.correct_questions = 0
        self.tim = TextInputManager()

    def reset(self) -> None:
        self.total_questions = 0
        self.correct_questions = 0

    def take_input(self, keys: ScancodeWrapper, events: list[Event], dt_s: float) -> None:
        self.tim.update(events=events, dt_s=dt_s)

    def update(self, dt_s: float):
        pass

    def draw(self, screen: pg.Surface):
        screen.fill((0, 0, 0))
        draw_text(
            surface=screen, pos=(WN_W // 2, WN_H // 2), horiz_align='left', vert_align='centre', text=f'Text Input: {self.tim.buf}',
            colour=(255, 255, 255), font_family=(self.game.assets.font_path, 18)
        )
