import pygame as pg

class Game:
    def __init__(self) -> None:
        self.prev_keys = pg.key.get_pressed()
