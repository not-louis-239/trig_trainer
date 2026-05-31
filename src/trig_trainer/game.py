import pygame as pg

from .asset_manager import Assets

from .states import (
    StateID,
    State,
    MenuState,
    GameState
)

class Game:
    def __init__(self) -> None:
        self.prev_keys = pg.key.get_pressed()
        self.assets = Assets()

        self.states: dict[StateID, State] = {
            StateID.MENU: MenuState(game=self),
            StateID.GAME: GameState(game=self)
        }
        self.state: StateID = StateID.GAME

    def take_input(self, keys: pg.key.ScancodeWrapper, events: list[pg.event.Event], dt_s: float) -> None:
        self.states[self.state].take_input(keys=keys, events=events, dt_s=dt_s)

    def update(self, dt_s: float):
        self.states[self.state].update(dt_s=dt_s)

    def draw(self, screen: pg.Surface):
        self.states[self.state].draw(screen=screen)
