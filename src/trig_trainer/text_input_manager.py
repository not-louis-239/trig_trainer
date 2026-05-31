import pygame as pg

class TextInputManager:
    def __init__(self) -> None:
        self.buf: str = ""
        self.last_submitted: str = ""
        pg.key.start_text_input()

    def update(self, events: list[pg.event.Event]) -> None:
        for event in events:
            if event.type == pg.TEXTINPUT:
                self.buf += event.text

            elif event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
                self.buf = self.buf[:-1]

            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                self.last_submitted = self.buf
                self.buf = ""
