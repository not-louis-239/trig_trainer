import pygame as pg

BACKSPACE_DELAY = 0.5
BACKSPACE_REPEAT = 0.075

class TextInputManager:
    def __init__(self) -> None:
        self.buf: str = ""
        self.last_submitted: str = ""

        self.backspace_held: bool = False
        self.backspace_timer: float = BACKSPACE_DELAY

        pg.key.start_text_input()

    def update(self, events: list[pg.event.Event], dt_s: float) -> None:
        for event in events:
            if event.type == pg.TEXTINPUT:
                self.buf += event.text

            elif event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
                self.backspace_held = True
                self.buf = self.buf[:-1]
                self.backspace_timer = BACKSPACE_DELAY

            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                self.last_submitted = self.buf
                self.buf = ""

            elif event.type == pg.KEYUP:
                if event.key == pg.K_BACKSPACE:
                    self.backspace_held = False
                    self.backspace_timer = BACKSPACE_DELAY

        if self.backspace_held:
            self.backspace_timer -= dt_s
            while self.backspace_timer <= 0:
                self.buf = self.buf[:-1]
                self.backspace_timer += BACKSPACE_REPEAT

