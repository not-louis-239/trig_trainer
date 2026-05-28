import sys
from pathlib import Path

import pygame as pg

sys.path.insert(0, str(Path(__file__).parent / "src"))

def main():
    scr = pg.display.set_mode((1100, 800))
    pg.display.set_caption("Trig Trainer")
    clock = pg.time.Clock()

    while True:
        events = pg.event.get()
        dt_s = clock.tick(60) / 1_000

        for event in events:
            if event.type == pg.QUIT:
                return

        scr.fill((255, 255, 255))
        pg.display.flip()

if __name__ == "__main__":
    main()
